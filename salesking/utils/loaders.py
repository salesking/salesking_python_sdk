#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import os
import logging
import json

try:
    import simplejson as json
except ImportError:
    import json

from salesking.utils.schema import _value_properties_are_referenced
from salesking.utils.schema import _value_is_required
from salesking.utils.schema import _value_is_type_text
from salesking.utils.schema import _value_is_default_any
from salesking.utils.schema import _value_has_items_key


from salesking.exceptions import SalesKingException
from salesking.conf.settings import SCHEMA_ROOT


log = logging.getLogger(__name__)


class SchemaStorage(object):
    """
    stores the loaded schemes by their referenced names
    """

    def __init__(self):
        self._schemes = {}

    def is_stored(self, name):
        return (name in self._schemes.keys() and
                self._schemes[name] is not None)

    def get_from_store(self, name):
        return self._schemes[name]

    def copy_to_store(self, name, json_obj):
        msg = u"adding %s to storage" % (name)
        # print msg
        if json_obj is None:
            raise Exception(u"%s is None no obj" % name)
        # validate the thing before storing
        if not self.is_stored(name):
            self._schemes[name] = copy.deepcopy(json_obj)
            # print self.stored_count()

    def stored_count(self):
        return len(self._schemes)

    def _has_no_ref_included(self, json_obj):
        pass

# make the loader a stack
JsonSchemaStore = SchemaStorage()
LoadingDict = {}


def _check_schema_file_content_for_reference_to_json(fs):
    """
    checks file contents fs for .json
    :param fs:
    :return: True/False
    """
    """
    :param fs:
    :return:
    """
    seek = u".json"
    if fs.find(seek) != -1:
        return False
    return True


def _load_referenced_schemes_from_list(the_list, val, a_scheme, a_property):
    """
    takes the referenced files and loads them
    returns the updated schema
    :param the_list:
    :param val:
    :param a_scheme:
    :param a_property:
    :return:
    """
    scheme = copy.copy(a_scheme)
    new_list = []
    for an_item in the_list:
        sub_scheme_name = generate_schema_name_from_uri(an_item['$ref'])
        content = load_schema(sub_scheme_name)
        new_list.append(content)

    scheme['properties'][a_property]['items'] = new_list
    return scheme


def _load_referenced_schema_from_properties(val, a_scheme, a_property):
    """
    :return: updated scheme
    """
    scheme = copy.copy(a_scheme)
    if _value_properties_are_referenced(val):
        ref_schema_uri = val['properties']['$ref']
        sub_schema = load_ref_schema(ref_schema_uri)
        ## dereference the sub schema
        sub_schema_copy_level_0 = copy.deepcopy(sub_schema)

        # nesting level 1
        # @TODO: NEEDS REFACTOR
        for prop_0 in sub_schema_copy_level_0['properties']:
            val_0 = sub_schema_copy_level_0['properties'][prop_0]
            # arrays may contain the nesting
            is_type_array_0 = (val_0['type'] == 'array')
            is_type_object_0 = (val_0['type'] == 'object')
            if ((is_type_array_0 or is_type_object_0)
                and (_value_properties_are_referenced(val_0))):
                # found a nested  thingy
                sub_schema_copy_level_1 = _load_referenced_schema_from_properties(val_0, sub_schema_copy_level_0,
                                                                                  prop_0)
                ###
                # one more loop level
                ###
                for prop_1 in sub_schema_copy_level_1['properties']:
                    val_1 = sub_schema_copy_level_1['properties'][prop_1]
                    is_type_array_1 = (val_1['type'] == 'array')
                    is_type_object_1 = (val_1['type'] == 'object')
                    if ((is_type_array_1 or is_type_object_1) and
                            (_value_properties_are_referenced(val_1))):
                        ### need to figure out a better way for loading
                        # the referenced stuff
                        # found a nested  thingy
                        # sub_schema_copy_level_2 = _load_referenced_schema_from_properties(val_1, sub_schema_copy_level_1, prop_1)
                        raise SalesKingException("too much nesting in the schemes")

            if _value_is_required(val_0):
                # remove required
                sub_schema_copy_level_0['properties'][prop_0]['required'] = False
            # hack to bypass text format valitation to string
            if _value_is_type_text(val_0):
                log.debug("patched text to string")
                sub_schema_copy_level_0['properties'][prop_0]['type'] = u"string"


        # outer scheme
        scheme['properties'][a_property]['properties'] = sub_schema_copy_level_0['properties']

    return scheme


def import_schema_to_json(name, store_it=False):
    """
    loads the given schema name
    from the local filesystem
    and puts it into a store if it
    is not in there yet
    :param name:
    :param store_it: if set to True, stores the contents
    :return:
    """

    schema_file = u"%s.json" % name
    file_path = os.path.join(SCHEMA_ROOT, schema_file)
    log.debug(u"trying to load %s " % file_path)
    schema = None
    try:
        schema_file = open(file_path, "r").read()
    except IOError, e:
        log.error(u"file not found %s" % e)
        msg = "Could not find schema file. %s" % file_path
        raise SalesKingException("SCHEMA_NOT_FOUND", msg)

    if not JsonSchemaStore.is_stored(name):
        schema = json.loads(schema_file)
        if schema is not None and store_it:
            JsonSchemaStore.copy_to_store(name, schema)

    if JsonSchemaStore.is_stored(name):
        schema = JsonSchemaStore.get_from_store(name)

    if schema is None:
        msg = "loading failed foo %s" % name
        raise SalesKingException("SCHEMA_NOT_FOUND", msg)

    return schema


def generate_schema_name_from_uri(ref_schema_uri):
    return ref_schema_uri.split("/")[1].split("#")[0].split(".")[0]


def load_ref_schema(ref_schema_uri):
    """
    loads a referenced schema
    """
    sub_schema = generate_schema_name_from_uri(ref_schema_uri)
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
    for prop in schema['properties']:
        value = schema['properties'][prop]
        # arrays may contain the nesting
        is_type_array = (value['type'] == 'array')
        is_type_object = (value['type'] == 'object')
        if ((is_type_array or is_type_object)
            and (_value_properties_are_referenced(value))):
            schema = _load_referenced_schema_from_properties(value, schema, prop)

        if is_type_array and _value_is_default_any(value) and _value_has_items_key(value):
            # print "value %s" % value
            schema = _load_referenced_schemes_from_list(value['items'], value, schema, prop)

        if _value_is_required(value):
            # remove required
            schema['properties'][prop]['required'] = False
        
        # hack to bypass text format valitation to string
        if _value_is_type_text(value):
            log.debug("patched text to string")
            schema['properties'][prop]['type'] = u"string"
        
        #ignore the readonly properties auto validation
        #if 'readonly' in value.keys() and value['readonly'] == True:
        #    log.debug("patched required validation to none required")
        #    schema['properties'][property]['readonly'] = False

    # sk works on title and not name
    schema['name'] = schema['title']
    ## go one level deeper as we now have some replacements



    return schema


def load_schema_raw(name):
    """
    loads the json schema and all referenced schemas 
    then converts to dict 
    """
    json_obj = load_schema(name)
    return json_obj


def build_loading_map(name, level=1):
    schema_file = u"%s.json" % name
    file_path = os.path.join(SCHEMA_ROOT, schema_file)
    log.debug(u"trying to load %s " % file_path)
    schema = None
    try:
        schema_file = open(file_path, "r").read()
    except IOError, e:
        log.error(u"file not found %s" % e)
        msg = "Could not find schema file. %s" % file_path
        raise SalesKingException("SCHEMA_NOT_FOUND", msg)
    schema = json.loads(schema_file)
    is_new_schema = (name not in LoadingDict.keys())

    if is_new_schema:
        LoadingDict[name] = []

    for a_property in schema['properties']:
        value = schema['properties'][a_property]
        # arrays may contain the nesting
        is_type_array = (value['type'] == 'array')
        is_type_object = (value['type'] == 'object')
        if is_type_array or is_type_object:
            if (('properties' in value.keys()) and
                    ('$ref' in value['properties'].keys())):
                ref_schema_uri = value['properties']['$ref']
                sub_schema_name = generate_schema_name_from_uri(ref_schema_uri)

                if sub_schema_name not in LoadingDict[name]:
                    LoadingDict[name].append(sub_schema_name)

    level += 1
    max_level = level
    for i, to_load_schema in enumerate(LoadingDict[name]):
        msg = "schema: %s %s to_load_schema %s L:%s" % (name, i, to_load_schema, level)
        print msg
        build_loading_map(to_load_schema, level=level)

    if level == 2:
        already_processed = []
        # nesting level 4
        for i, a_key in enumerate(LoadingDict.keys()):

            # @todo: improve the iteration
            if len(LoadingDict[a_key]) == 1:
                a_sub_schema_name = LoadingDict[a_key][0]
                if not a_sub_schema_name in already_processed:
                    msg = "loading: sub %s" % a_sub_schema_name
                    print msg
                    load_schema(a_sub_schema_name)
                    already_processed.append(a_sub_schema_name)

                if not a_key in already_processed:
                    msg = "loading: key %s" % a_key
                    print msg
                    load_schema(a_key)
                    already_processed.append(a_key)

                    # nesting level 3
                    #for i, a_key in enumerate(LoadingDict.keys()):
                    #    # @todo: improve the iteration
                    #    if LoadingDict[a_key].len() == 2:
                    #        load_schema(LoadingDict[a_key][LoadingDict[a_key].len()-1])
                    #        load_schema(a_key)




