#!/usr/bin/env python
# -*- coding: utf-8 -*-

from salesking.utils import load_schema, pluralize
from salesking.tests.base import SalesKingBaseTestCase
from salesking.exceptions import SalesKingException

class SKUtilsTestCase(SalesKingBaseTestCase):
    
    def test_load_client_schema_success(self):
        a_json = load_schema(u"client")
        self.assertTrue(a_json!=None)
        self.assertTrue(a_json['type']!=None)
    
    def test_load_schema_fails(self):
        thrown = False
        try:
            load_schema("notexisting");
        except SalesKingException, e:
            if (e.code == "SCHEMA_NOTFOUND"):
               thrown=True
        self.assertTrue(thrown)
        
    def test_pluralize(self):
        self.assertEquals("clients",pluralize("client"));
        self.assertEquals("companies",pluralize("company"));

