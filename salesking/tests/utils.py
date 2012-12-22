#!/usr/bin/env python
# -*- coding: utf-8 -*-

from salesking.utils import loaders, helpers, validators 
from salesking.tests.base import SalesKingBaseTestCase
from salesking.exceptions import SalesKingException

class SKUtilsTestCase(SalesKingBaseTestCase):
    
    def test_load_client_schema_success(self):
        a_json = loaders.load_schema(u"client")
        self.assertTrue(a_json != None)
        self.assertTrue(a_json['type'] != None)
    
    def test_load_schema_fails(self):
        thrown = False
        try:
            loaders.load_schema("notexisting");
        except SalesKingException, e:
            if (e.code == "SCHEMA_NOTFOUND"):
               thrown=True
        self.assertTrue(thrown)
        
    def test_pluralize(self):
        self.assertEquals("clients", helpers.pluralize("client"));
        self.assertEquals("companies", helpers.pluralize("company"));
        
    def test_json_schema_validation_datetime_pass(self):
        schema = {u'format': u'date-time'}
        self.assertEquals(None, validators.json_schema_validation_format(u"2012-12-19T00:39:49+01:00", schema));
        self.assertEquals(None, validators.json_schema_validation_format(u"2012-12-19T00:39:49", schema));

