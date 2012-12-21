#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
try:
    import simplejson as json
except ImportError:
    import json
from urllib import urlencode

from salesking.exceptions import SalesKingException
from salesking import utils 
from salesking.resources import API_BASE_PATH
from salesking import resources
from jsonschema import _flatten

DEFAULT_TYPES = {
        "array" : list, "boolean" : bool, "integer" : int, "null" : type(None),
        "number" : (int, float), "object" : dict, "string" : basestring,
        
}

log=logging.getLogger(__name__)


class CollectionAttributesMixin(object):
    """
    Container for all the Collection Attributes
    """
    __api__ = None
    
    def __init__(self, resource_type, api, **kwargs):
        self.__api__ = api
        if isinstance(resource_type,dict):
            self.resource_type = resource_type['type']
        else:
            self.resource_type = resource_type
        self.schema = utils.load_schema_raw(self.resource_type) 
        self.autoload = False
        self.filters = dict()
        self.items = []
        self.current_page = None
        self.total_pages = None
        self.total_entries = None
        self.per_page = 100
        self.sort = u"ASC"
        self.sort_by = None
        self._types = DEFAULT_TYPES # type mapping

    
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
        set entries per page max 100
        """
        if isinstance(int,entries) and entries <=100:
            self.per_page = int(entries)
            return self
        else:
            raise SaleskingException("PERPAGE_ONLYINT","Please set an integer <100 for the per-page limit");
 
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
        get all items
        """
        return self.items
    
    def get_resource_type(self):
        """
        get type
        """
        return self.resource_type
    
    def set_resource_type(self,klass):
        """
        set type and load schema
        """
        self.resource_type = klass
        self.schema = utils.load_schema_raw(self.resource_type)

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
        if self.validate_filter(key,filter_value):
            self.filters[key]=filter_value
            return True
        else:
            raise SaleskingException("FILTER_INVALID",'Invalid filter value: filter:%s value:%s' % (key,filter_value))
    
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
    
    def validate_filter(self,key,filter_value):
        """
        validate the filter key and value
        """
        ok = False
        seek = u"filter[%s]" % key
        schema = None
        value  = None
        for link in self.schema['links']:
            if link['rel'] == 'instances':
               for property in link['properties']:
                   if seek == property:
                       value = link['properties'][property]
                       ok = True
        if not ok:
            return False
        ok = self._is_type(filter_value, value['type'])
        return ok
    
    def get_filters(self):
        return self.filters
    
    def _pre_load(self, page = None):
        """
        builds the url to call
        """
        query = []
        # build the filters
        for filter,value in self.filters:
            query_str = u"%s=%s" % (filter,urlencode(value))
            query.append(query_str)
        if self.sort:
            query_str = u"%s=%s" % (u"sort",self.sort)
            query.append(query_str)
        if self.sort_by:
            query_str = u"%s=%s" % (u"sort_by",self.sort_by)
            query.append(query_str)
        if self.per_page:
            query_str = u"%s=%s" % (u"per_page",self.per_page)
            query.append(query_str)
        if page:
            query_str = u"%s=%s" % (u"page",page)
            query.append(query_str)
        query = u"?%s" % (u"&".join(query))
        url = u"%s%s" % (self.get_list_endpoint()['href'],query)
        url = u"%s%s%s" % (self.__api__.base_url, API_BASE_PATH,url)
        msg = "_pre_load: url:%s" % url
        log.debug(msg)
        print msg
        return url
    
    def get_list_endpoint(self, rel=u"instances"):
        """
        get the configured list entpoint for the schema.type
        """
        schema_loaded = not self.schema is None
        links_present = "links" in self.schema.keys()
        if (schema_loaded and links_present):
             for row in self.schema['links']:
                  if row['rel'] == rel:
                      #print "row %s" % row
                      return row
        raise APIException("ENDPOINT_NOTFOUND","invalid endpoint")
    
    def _load(self,url):
        raise Exception("implemnt in subclass please")
    
    def _post_load(self,response):
        """
        post load processing
        """
        if response is not None and response.status_code == 200:
            types = utils.pluralize(self.resource_type)
            body = json.loads(response.content, encoding='utf-8')
            self.total_entries = body['collection']['total_entries']
            self.total_pages = body['collection']['total_pages']
            self.current_page = body['collection']['current_page']
            ## now get the items from the class factory
            for object in body[types]:
                item_cls = resources.get_model_class(self.resource_type)
                properties_dict = object[self.resource_type]
                new_dict = utils.remove_properties_containing_None(properties_dict)
                item = item_cls(new_dict,api=self.__api__)
                ## add the items
                self.items.append(item)
            #autoload is true, so lets fetch all the other pages recursivly
            if(self.autoload == True and self.total_pages > 1 and page == None):
                for x in xrange(2,self.total_pages):
                    self.load(x)
            return self
        else:
            raise SalesKingException("LOAD_ERROR","Fetching failed, an error happend",response)
    

class CollectionResource(CollectionAttributesMixin):
    """
    Resource collection representing answers form the api
    """    
    
    def load(self,page = None):
        """
        call to execute the collection loading
        """
        url = self._pre_load(page)
        response = self._load(url)
        response = self._post_load(response)
        return response
        
    def _load(self, url):
        """
        Execute a request against the Salesking API to fetch the items
        :param int $page page number to fetch
        :return SaleskingCollection
        :raises SaleskingException
        """
        msg = "_load: %s" % url
        log.debug(msg)
        print msg
        response = self.__api__.request(url)
        return response
        
def get_collection_instance(klass, api = None,**kwargs):
    _type = klass
    if isinstance(klass, dict):
        _type = klass['type']
    #schema = load_schema_raw(_type)
    obj = CollectionResource(_type, api,**kwargs)
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

    def sort(self,direction="ASC"):
        """
        set the sort to the query
        """
        direction=directtion.upper()
        if direction in ['ASC','DESC']:
            self.sort = direction
        else:
            raise SaleskingException("SORT_INVALIDDIRECTION","Invalid sorting direction - please choose either ASC or DESC");
    
    def sort_by(self, property):
        """
        set sort by property to the query
        """
        seek ="sort_by"
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
    