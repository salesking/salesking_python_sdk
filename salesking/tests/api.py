#!/usr/bin/env python
# -*- coding: utf-8 -*-

from salesking import api    
from salesking.tests.base import SalesKingBaseTestCase


class SKApiTestCase(SalesKingBaseTestCase):
    
#    def test_access_token_fail(self):
#        clnt = api.APIClient()
#        token = clnt.request_access_token("dummy")
#        msg ="response:%s" % token
#        self.assertTrue(token!=None, msg)
        
    def test_basic_auth_raw_sk_client_get_success(self):
        clnt = api.APIClient()
        url ="%s/api/contacts" % clnt.base_url
        response = clnt.request(url)
        self.assertEquals(response.status_code,200)
        msg ="response: %s" % response.text
        self.assertEquals(response.text.find("error"),-1,msg)
