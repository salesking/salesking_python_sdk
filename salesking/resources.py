#!/usr/bin/env python
# -*- coding: utf-8 -*-

#see for the ideas
# https://github.com/dstufft/slumber
# https://github.com/bcwaldon/warlock
## check sluber
## check warlock

"""
    Initial API based on slumber and warlock
    thanks guys
"""
    
import sys
import os
import logging
from StringIO import StringIO
import logging
import copy
try:
    import simplejson as json
except ImportError:
    import json

from warlock import model_factory
from warlock.model import Model
from salesking import exceptions

from salesking.utils import loaders, helpers
from salesking.exceptions import SalesKingException
from salesking.api import APIClient



log = logging.getLogger(__name__)

API_BASE_PATH = u'api/'


class Resource(Model):
    """
    General Flow for load, save, delete
    """
    def _save(self,*args,**kwargs):
        raise Exception("Please implement _save() in subclass")
    
    def _delete(self,id,*args,**kwargs):
        raise Exception("Please implement _save() in subclass")
    
    def _load(self,id,*args,**kwargs):
        raise Exception("Please implement _save() in subclass")
    
    def _pre_save(self,*args,**kwargs):
        """
        pre save hook
        """
        pass
    
    def _post_save(self,response,*args,**kwargs):
        """
        post save hook
        """
        return response
    
    def save(self, *args, **kwargs):
        """
        saves creates or updates current resource
        returns new resource
        """
        self._pre_save(*args, **kwargs)
        response = self._save(*args, **kwargs)
        response = self._post_save(response, *args, **kwargs)
        return response
    
    def _pre_load(self,id,*args,**kwargs):
        """
        pre load hook
        """
        pass
    
    def _post_load(self,response,*args,**kwargs):
        """
        post laod hook
        """
        return response
    
    def load(self, id, *args, **kwargs):
        """
        loads a remote resource by id
        """
        self._pre_load(*args, **kwargs)
        response = self._load(*args, **kwargs)
        response = self._post_load(response, *args, **kwargs)
        return response
    
    def _pre_delete(self, *args,**kwargs):
        """
        pre delete hook
        """
        pass
    
    def _post_delete(self, response,*args,**kwargs):
        """
        post delete hook
        """
        return response
    
    def delete(self,  *args, **kwargs):
        """
        deletes current resource
        returns response from api
        """
        self._pre_delete(*args, **kwargs)
        response = self._delete(*args, **kwargs)
        response = self._post_delete(response, *args, **kwargs)
        return response


class BaseResource(Resource):
    __api__ = None 
    
    def get_id(self):
        """
        Model may have an unset id
        id is used to determine if it is a save or update
        """
        id = None
        try:
            id = self.__getattr__(u'id')
        except:
            pass
        return id
        
    def get_data(self):
        """
        put the object to json and remove the internal stuff
        """
        data = json.dumps(self)
        out = u'{"%s":%s}' % (self.schema['title'],data)
        return out
    
    def get_endpoint(self, rel=u"self"):
        schema_loaded = not self.schema is None
        links_present = "links" in self.schema.keys()
        if (schema_loaded and links_present):
             for row in self.schema['links']:
                  if row['rel'] == rel:
                      #print "row %s" % row
                      return row
        raise APIException("ENDPOINT_NOTFOUND","invalid endpoint")
    
    def get_resource_remote_schema(self):
        response = self._do_api_call(call_type="schema")
        return response
    
    def _try_to_serialize(self,response):
        return response


class RemoteResource(BaseResource):
    """
    Resource dealing with the api and transportation
    self.load(id)
    self.save()
    self.delete()
    
    """

    def __repr__(self):
        return u'<RemoteResource id:%s>' %(self.get_id())
    
    def _save(self):
        is_update = self.get_id() is not None 
        if is_update:
            call_type='update'
        else:
            call_type='create'
        response = self._do_api_call(call_type=call_type, id=self.get_id())
        return response
    
    def _load(self,id = None):
        response = self._do_api_call(call_type="load", id=id)
        return response
    
    def _delete(self):
        response = self._do_api_call(call_type="delete", id=self.get_id())
        return response
    
    
    def _do_api_call(self, call_type=u'', id=None):
        """
        returns a response if it is a valid call
        otherwise the corresponding error
        
        """
        endpoint = None
        url = None
        if call_type == u'load':
            endpoint = self.get_endpoint("self")
            if id is None:
                raise APIException("LOAD_IDNOTSET","could not load object")
        elif call_type == u'delete':
            endpoint = self.get_endpoint("destroy")
            if id is None:
                raise APIException("DELETE_IDNOTSET","could not delete object")
        elif call_type == u'update':
            endpoint = self.get_endpoint("update")
            if id is None:
                raise APIException("UPDATE_IDNOTSET","could not load object")
        elif call_type == u'create':
            endpoint = self.get_endpoint("create")
            url = u"%s%s%s" % (self.__api__.base_url, API_BASE_PATH, endpoint['href'])
        elif call_type == u'schema':
            # add schema gethering functionality 
            # hackisch
            endpoint = self.get_endpoint("create")
            url = u"%s%s%s/schema" % (self.__api__.base_url, API_BASE_PATH, endpoint['href'])
            endpoint['method'] = u'GET'    
        if id is not None:
            url = u"%s%s%s" % (self.__api__.base_url, API_BASE_PATH, endpoint['href'].replace(u"{id}",id))
        ## exceute the api request
        payload = self.get_data()
        method = endpoint['method']
        # request raises exceptions if something goes wrong
        obj = None
        try:
            response = self.__api__.request(url, method, data=payload)
            #load update create success
            if ((response.status_code == 200 and 
                 call_type in ['load','update']) or 
            (response.status_code == 201 and call_type == 'create')):
                msg ="call_type: %s successfully completed" % call_type
                log.info(msg)
                return self.get_object_from_response(response)
            elif (response.status_code == 200 and call_type in ['delete']):
            #delete success
                msg ="call_type: %s successfully completed" % call_type
                log.info(msg)
                return self._try_to_serialize(response)
            elif 200 <= response.status_code <= 299:
                return self._try_to_serialize(response)
        except Exception, e:
            msg ="Exception occoured %s url: %s" % (e,url)
            log.error(msg)
            raise e
        
    def get_object_from_response(self, response):
        """
        transforms the response into a new object
        :param response: valid respone status code 200
        :returns new instance of current class
        """
        klass = self.schema['title']
        cls = get_model_class(klass, api=self.__api__)
        jdict = json.loads(response.content, encoding="utf-8")
        ### check if we have a response
        properties_dict = jdict[self.schema['title']]
        new_dict = helpers.remove_properties_containing_None(properties_dict)
        obj = cls(new_dict)
        return obj
    
      

def get_model_class( klass, api = None, use_request_api = True):
    """
    Generates the Model Class based on the klass 
    loads automatically the corresponding json schema file form schemes folder
    :param klass: json schema filename
    :param use_request_api: if True autoinitializes request class if api is None
    :param api: the transportation api
                if none the default settings are taken an instantiated
    """
    if api is None and use_request_api:
        api = APIClient()
    _type = klass
    if isinstance(klass, dict):
        _type = klass['type']
    schema = loaders.load_schema_raw(_type)
    model_cls = model_factory(schema, base_class = RemoteResource)
    model_cls.__api__ = api
    return model_cls

