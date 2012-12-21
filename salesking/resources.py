#see for the ideas
# https://github.com/dstufft/slumber
# https://github.com/bcwaldon/warlock
## check sluber
## check warlo

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

from salesking.utils import load_schema_raw, remove_properties_containing_None
from salesking.exceptions import SalesKingException



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
    #id = None #readonly
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
    """
    def __repr__(self):
        return u'<RemoteResource %s> %s' %(self.get_id(),self.schema)
    
    
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
        # request raises exceptions if not 200
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
        except Exception,e:
            msg ="Exception occoured %s" % e
            log.error(msg)
            raise e
        
    def get_object_from_response(self, response):
        klass = self.schema['title']
        cls = get_model_class(klass, api=self.__api__)
        jdict = json.loads(response.content, encoding="utf-8")
        ### check if we have a response
        
        properties_dict = jdict[self.schema['title']]
        new_dict = remove_properties_containing_None(properties_dict)
        obj = cls(new_dict)
        return obj
    
      

def get_model_class( klass, api = None):
    _type = klass
    if isinstance(klass, dict):
        _type = klass['type']
    schema = load_schema_raw(_type)
    model_cls = model_factory(schema, base_class = RemoteResource)
    model_cls.__api__ = api
    return model_cls



    
    


#class CallableMixin(object):
#    """
#    Resource provides the main functionality behind slumber. It handles the
#    attribute -> url, kwarg -> query param, and other related behind the scenes
#    python to HTTP transformations. It's goal is to represent a single resource
#    which may or may not have children.
#
#    It assumes that a Meta class exists at self._meta with all the required
#    attributes.
#    """
#
#    def __init__(self, *args, **kwargs):
#        self._store = kwargs
#
#    def __call__(self, id=None, format=None, url_override=None):
#        """
#        Returns a new instance of self modified by one or more of the available
#        parameters. These allows us to do things like override format for a
#        specific request, and enables the api.resource(ID).get() syntax to get
#        a specific resource by it's ID.
#        """
#
#        # Short Circuit out if the call is empty
#        if id is None and format is None and url_override is None:
#            return self
#
#        kwargs = {}
#        for key, value in self._store.iteritems():
#            kwargs[key] = value
#
#        if id is not None:
#            kwargs["base_url"] = url_join(self._store["base_url"], id)
#
#        if format is not None:
#            kwargs["format"] = format
#
#        if url_override is not None:
#            # @@@ This is hacky and we should probably figure out a better way
#            #    of handling the case when a POST/PUT doesn't return an object
#            #    but a Location to an object that we need to GET.
#            kwargs["base_url"] = url_override
#
#        kwargs["session"] = self._store["session"]
#
#        return self.__class__(**kwargs)
    
    
















#class ResourceProxy(object):
#    """Proxy object to a resource
#
#    It lazily fetches data.
#    """
#
#    def __init__(self, url, service, api):
#        self._url = url
#        self._service = service
#        self._api = api
#        self._type, id = self._service.parse_resource_url(self._url)
#        self._id = int(id)
#        self._resource = None
#
#    def __repr__(self):
#        if self._resource:
#            return repr(self._resource)
#        else:
#            return '<ResourceProxy %s/%s>' % (self._type, self._id)
#
#    def __getattr__(self, attr):
#        return getattr(self._get(), attr)
#
#    def __getitem__(self, item):
#        return self._get()[item]
#
#    def __contains__(self, attr):
#        return attr in self._get()
#
#    def _get(self):
#        """Load the resource
#        
#        Do nothing if already loaded.
#        """
#        if not self._resource:
#            self._resource = self._api(self._type, self._id)
#        return self._resource
#
#
#class Resource(object):
#    """A fetched resource"""
#
#    def __init__(self, resource, type, id, url):
#        self._resource = resource
#        self._type = type
#        self._id = id
#        self._url = url
#
#    def __repr__(self):
#        return '<Resource %s: %s>' % (self._url, self._resource)
#
#    def __getattr__(self, attr):
#        if attr in self._resource:
#            return self._resource[attr]
#        else:
#            raise AttributeError(attr)
#    
#    def __getitem__(self, item):
#        if item in self._resource:
#            return self._resource[item]
#        else:
#            raise KeyError(item)
#
#    def __contains__(self, attr):
#        return attr in self._resource