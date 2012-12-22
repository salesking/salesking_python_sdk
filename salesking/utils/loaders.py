import copy
import sys
import os
import logging

try:
    import simplejson as json
except ImportError:
    import json

from StringIO import StringIO

from salesking.exceptions import SalesKingException
from salesking.conf.settings import SCHEMA_ROOT


log = logging.getLogger(__name__)


def import_schema_to_json(name):
    schema_file = u"%s.json" % name
    schema = None
    file_path = os.path.join(SCHEMA_ROOT,schema_file)
    log.debug(u"trying to load %s " % file_path)
    try:
        schema_file = open(file_path,"r").read()
    except IOError,e:
        log.error(u"file not found %s" % e)
        msg = "Could not find schema file. %s" % file_path
        raise SalesKingException("SCHEMA_NOTFOUND",msg)
    schema = json.loads(schema_file)
    return copy.deepcopy(schema)

def load_ref_schema(ref_schema_uri):
    """
    loads a referenced schema
    """
    sub_schema = ref_schema_uri.split("/")[1].split("#")[0].split(".")[0]
    return import_schema_to_json(sub_schema)

def load_schema(name):
    """ 
    loads the schema by name
    :param name name of the model
    """
    schema = import_schema_to_json(name)
    #salesking specific swap
    #//set link relation as key name to make it easier to call these
    for item in schema['links']:
        #//set link relation as key name to make it easier to call these
        #            foreach($schema->links as $key => $link)
        #            {
        #                $schema->links[$link->rel] = $link;
        #                unset($schema->links[$key]);
        #            }
        # this here seems not to work as expected
        # something is wrong
        href_value = item['href']
        rel_value = item['rel']
        schema[rel_value] = href_value
        del item
    ## sk use nesting of schema
    ## dynamically loading
    for property in schema['properties']:
        value = schema['properties'][property]
        # arrays may contain the nesting
        if (value['type'] == 'array'):
            if '$ref' in value['properties'].keys():
                ref_schema_uri=value['properties']['$ref']
                sub_schema = load_ref_schema(ref_schema_uri)
                schema['properties'][property]['properties'] = copy.deepcopy(sub_schema['properties'])
        #ignore the required properties auto validation
        #otherwise the json instnaciation breaks
        if 'required' in value.keys() and value['required'] == True:
            log.debug("patched required validation to False - asllowing auto schema validation")
            schema['properties'][property]['required'] = False
        #ignore the readonly properties auto validation
        #if 'readonly' in value.keys() and value['readonly'] == True:
        #    log.debug("patched required validation to none required")
        #    schema['properties'][property]['readonly'] = False

    # sk works on title and not name
    schema['name'] = schema['title']
    return schema


def load_schema_raw(name):
    """
    loads the json schema and all referenced schemas 
    then converts to dict 
    """
    json_obj = load_schema(name)
    return json_obj