#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import logging
from StringIO import StringIO

try:
    import simplejson as json
except ImportError:
    import json

def pluralize(data_type):
    """
    adds s to the data type or the correct english plural form
    """
    known = {
             u"address": u"addresses", 
             u"company": u"companies"
    }
    if data_type in known.keys():
        return known[data_type]
    else:
        return u"%ss" % data_type
    
def remove_properties_containing_None(properties_dict):
    """
    removes keys from a dict those values == None
    json schema validation might fail if they are set and
    the type or format of the property does not match
    """
    # remove empty properties - as validations may fail
    new_dict  = dict()
    for key in properties_dict.keys():
        value = properties_dict[key]
        if value is not None:
            new_dict[key] = value
    return new_dict

def json_to_py(j):
    o = json.loads(j)
    if isinstance(o, dict):
        return dict_to_object(o)
    else:
        return dict_to_object({ "response": o }).response

def dict_to_object(d):
    """Recursively converts a dict to an object"""
    top = type('CreateSendModel', (object,), d)
    seqs = tuple, list, set, frozenset
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, dict_to_object(j))
        elif isinstance(j, seqs):
            setattr(top, i, type(j)(dict_to_object(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top
  