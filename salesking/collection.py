#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

try:
    import simplejson as json
except ImportError:
    import json

from urllib import urlencode
from jsonschema import _flatten

# other jsonchema version
#from jsonschema import _utils

from salesking import resources, api
from salesking.exceptions import SalesKingException
from salesking.resources import API_BASE_PATH
from salesking.utils import validators, loaders, helpers


DEFAULT_TYPES = {
        "array" : list, "boolean" : bool, "integer" : int, "null" : type(None),
        "number" : (int, float), "object" : dict, "string" : basestring, 
        "text" : basestring,
}

log = logging.getLogger(__name__)


class CollectionAttributesMixin(object):
    """
    Container for all the Collection Attributes
    """
    __api__ = None
    
    def __init__(self, resource_type, api, **kwargs):
        self.__api__ = api
        if isinstance(resource_type, dict):
            self.resource_type = resource_type['type']
        else:
            self.resource_type = resource_type
        self.schema = loaders.load_schema_raw(self.resource_type) 
        self.filters = dict()
        self.current_page = None
        self.total_pages = None
        self.total_entries = None
        self.per_page = 100
        self.sort = u"ASC"
        self.sort_by = None
        self._items = []
        self._types = DEFAULT_TYPES # type mapping
        self._last_query_str = None

    def get_sort(self):
        """
        get sort direction
        """
        return self.sort
       
    def get_sort_by(self):
        """
        get sort by
        """
        return self.sort_by
    
    def set_per_page(self,entries = 100):
        """
        set entries per page max 200
        """
        if isinstance(entries, int) and entries <=200:
            self.per_page = int(entries)
            return self
        else:
            raise SaleskingException("PERPAGE_ONLYINT","Please set an integer <200 for the per-page limit");
 
    def get_per_page(self):
        """
        get per page
        """
        return self.per_page
    
    def get_total_entries(self):
        """
        get total entries
        """
        return self.total_entries
    
    def get_total_pages(self):
        """
        get total pages
        """
        return self.total_pages
    
    def get_current_page(self):
        """
        current page
        """
        return self.current_page
    
    def get_items(self):
        """
        :returns all fetched _items (RemoteResource Json classes)
        """
        return self._items
        
    
    def clear_items(self):
        """
        empties the items dict
        """
        self._items = []
        
    def get_resource_type(self):
        """
        get type to fetch
        """
        return self.resource_type
    
    def set_resource_type(self,klass):
        """
        set type to load and load schema
        """
        self.resource_type = klass
        self.schema = loaders.load_schema_raw(self.resource_type)

    def set_filters(self, filters):
        """
        set and validate filters dict
        """
        if not isinstance(filters, dict):
            raise Exception("filters must be a dict")
        self.filters = {}
        for key in filters.keys():
            value = filters[key]
            self.add_filter(key,value)
            
    def add_filter(self,key,filter_value):
        """
        add and validate a filter with value
        returns True on success otherwise exception
        """
        seek = u"filter[%s]" % key
        if self.validate_filter(key, filter_value):
            self.filters[key]=filter_value
            return True
        else:
            #print u"failed to validate: %s" % seek
            msg = u'Invalid filter value: filter:%s value:%s' % (key, filter_value)
            raise SalesKingException("FILTER_INVALID", msg )
    
    def _is_type(self, instance, type):
        """
        Check if an ``instance`` is of the provided (JSON Schema) ``type``.
        """
        if type not in self._types:
            raise UnknownType(type)
        type = self._types[type]

        # bool inherits from int, so ensure bools aren't reported as integers
        if isinstance(instance, bool):
            type = _flatten(type)
            if int in type and bool not in type:
                return False
        return isinstance(instance, type)

        
    def validate_filter(self, key, filter_value):
        """
        validate the filter key and value against the collection schema
        
        :param key: property name
        :param filter_value: value of the filter
        :returns True if all is ok otherwise False
        """
        ok = False
        seek = u"filter[%s]" % key
        schema = None
        value  = None
        is_string_with_format = False
        string_format = None
        for link in self.schema['links']:
            if link['rel'] == 'instances':
               for property in link['properties']:
                   if seek == property:
                       value = link['properties'][property]
                       ok = True
        if not ok:
            return False
        ok = self._is_type(filter_value, value['type'])
        # if string with type add validation
        if ok == True and value['type'] == 'string' and 'format' in value.keys():
            ok = self._validate_json_format(filter_value, value)
            
        return ok
    
    def _validate_json_format(self, filter_value, schema_validation_type):
        """
        adds the type:string format:schema_validation_type
        :param filter_value: value of the filter
        :param schema_validation_type: format description of the json schema entry
        """
        ok = False
        try:
            validators.json_schema_validation_format(filter_value, schema_validation_type)
            ok = True
        except ValueError as e:
            pass
        return ok
    
    def get_filters(self):
        return self.filters
    
    def _build_query_url(self, page = None, verbose = False):
        """
        builds the url to call
        """
        query = []
#        # build the filters
#        for afilter in self.filters.keys():
#            value = self.filters[afilter]
#            print"filter:%s value:%s" % (afilter,value)
#            value = urlencode(value)
#            query_str = u"%s=%s" % (afilter, value)
        if len(self.filters) > 0:
            query.append(urlencode(self.filters))
        if self.sort:
            query_str = u"%s=%s" % (u"sort", self.sort)
            query.append(query_str)
        if self.sort_by:
            query_str = u"%s=%s" % (u"sort_by", self.sort_by)
            query.append(query_str)
        if self.per_page:
            query_str = u"%s=%s" % (u"per_page", self.per_page)
            query.append(query_str)
        if page:
            query_str = u"%s=%s" % (u"page", page)
            query.append(query_str)
        query = u"?%s" % (u"&".join(query))
        url = u"%s%s" % (self.get_list_endpoint()['href'],query)
        url = u"%s%s%s" % (self.__api__.base_url, API_BASE_PATH, url)
        msg = "_build_query_url: url:%s" % url
        log.debug(msg)
        if verbose:
            print msg
        return url
    
    def get_list_endpoint(self, rel=u"instances"):
        """
        get the configured list entpoint for the schema.type
        :param rel: lookup rel: value inside the links section
        :returns the value
        :raises APIException
        """
        schema_loaded = not self.schema is None
        links_present = "links" in self.schema.keys()
        if (schema_loaded and links_present):
             for row in self.schema['links']:
                  if row['rel'] == rel:
                      #print "row %s" % row
                      return row
        raise APIException("ENDPOINT_NOTFOUND","invalid endpoint")
    
    def _load(self, url):
        raise Exception("implemnt in subclass please")
    
    def _post_load(self, response, verbose):
        """
        post load processing
        fills the self._items collection
        """
        try:
            if verbose:
                print response.content
            log.debug(response.content)
        except Exception, e:
            raise e
            
        if response is not None and response.status_code == 200:
            types = helpers.pluralize(self.resource_type)
            #print "types %s" % types
            body = json.loads(response.content, encoding='utf-8')
            self.total_entries = body['collection']['total_entries']
            self.total_pages = body['collection']['total_pages']
            self.current_page = body['collection']['current_page']
            ## now get the items from the class factory
            for response_item in body[types]:
                obj = self._response_item_to_object(response_item)
                ## add the items
                self._items.append(obj)
            
        else:
            msg = u"Fetching failed, an error happend"
            raise SalesKingException("LOAD_ERROR", msg, response)
        
        return self
    
    def _response_item_to_object(self, resp_item):
        """
        take json and make a resource out of it
        """
        item_cls = resources.get_model_class(self.resource_type)
        properties_dict = resp_item[self.resource_type]
        new_dict = helpers.remove_properties_containing_None(properties_dict)
        # raises exception if something goes wrong
        obj = item_cls(new_dict)
        return obj

class CollectionResource(CollectionAttributesMixin):
    """
    Resource collection representing answers form the api
    """    
    
    def load(self, page = None, verbose=False):
        """
        call to execute the collection loading
        :param page: integer of the page to load
        :param verbose: boolean to print to console
        :returns response
        :raises the SalesKingException
        """
        url = self._build_query_url(page, verbose)
        response = self._load(url, verbose)
        response = self._post_load(response, verbose)
        return response
        
    def _load(self, url, verbose):
        """
        Execute a request against the Salesking API to fetch the items
        :param url: url to fetch
        :return response
        :raises SaleskingException with the corresponding http errors
        """
        msg = u"_load url: %s" % url
        self._last_query_str = url
        log.debug(msg)
        if verbose:
            print msg
        response = self.__api__.request(url)
        return response
        
        
def get_collection_instance(klass, api_client = None, request_api=True, **kwargs):
    """
    instatiates the collection lookup of json type klass
    :param klass: json file name
    :param api_client: transportation api
    :param request_api: if True uses the default APIClient
    """
    _type = klass
    if api_client is None and request_api:
        api_client = api.APIClient()
    if isinstance(klass, dict):
        _type = klass['type']
    obj = CollectionResource(_type, api_client, **kwargs)
    return obj        
 
#
#    /**
#     * magic method for mapping all kinds of method calls to addFilter
#     * @param string $method method name
#     * @param array $args array of arguments
#     * @return SaleskingCollection
#     * @throws BadMethodCallException
#     * @since 1.0.0
#     */
#    public function __call($method, array $args) {
#        try {
#            $this->addFilter($method,$args[0]);
#            return $this;
#        }
#        catch (SaleskingException $e)
#        {
#            if($e->getCode() == "FILTER_NOTEXISTING")
#            {
#                throw new BadMethodCallException('Call to undefined method :'.$method);
#            }
#
#            throw $e;
#        }
#    }

    def sort(self, direction = "ASC"):
        """
        set the sort to the query
        ['ASC','DESC']
        """
        direction = directtion.upper()
        if direction in ['ASC','DESC']:
            self.sort = direction
        else:
            raise SaleskingException("SORT_INVALIDDIRECTION","Invalid sorting direction - please choose either ASC or DESC");
    
    def sort_by(self, property):
        """
        set sort by property to the query
        """
        seek =u"sort_by"
        # make sure that the api supports sorting for this kind of object
        if seek in self.schema['links']['instances']['properties']:
            #  make sure that we have a valid property
            if seek in self.schema['links']['instances']['properties']['sort_by']['enum']:
                self.sort_by = property
                return self
            else:
                raise SaleskingException("SORTBY_INVALIDPROPERTY","Invalid property for sorting");
        else:
            raise SaleskingException("SORTBY_CANNOTSORT","object type doesnt support sorting");
        
        
### date validation ###??
#//validate input format
#        if(property_exists($schema,"format"))
#        {
#            switch ($schema->format) {
#                case "date":
#                    if(!preg_match('/^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/',$value) AND $value != "")
#                    {
#                        return false;
#                    }
#                    break;
#                case "date-time":
#                    //@todo which date-tme format is accepted??
#                    break;
#            }
#        }
#
#        return true;
    