#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
try:
    from salesking.conf.local_settings import SALESKING_API
except ImportError,e:
    raise e
    raise Exception("please create a salesking.conf.local_settings")

# root of this packag
SK_ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# abspath where the schemes ares stored
SCHEMA_ROOT = os.path.join(SK_ROOT, "schemes")  

AUTH_URL = u"/oauth/authorize"
ACCESS_TOKEN_URL = u"/oauth/token"

API = {
       # YOUR APPID
       u"app_id": SALESKING_API['APP_ID'],
       # YOUR APP SECRET
       u"app_secret": SALESKING_API['APP_SECRET'],
       u"app_scope": u"api/clients:write",
       # YOUR SALESKING SUBDOMAIN
       u"sk_subdomain": u"frank",
       
       u"base_url": SALESKING_API['BASE_URL'],
       u"oauth_redirect_url": u"http://localhost/",
       u"debug": False,
       u"use_oauth": False,
       u"sk_user": SALESKING_API['SK_USER'],
       u"sk_pw": SALESKING_API['SK_PASSWORD']
}

#
#App ID
#    355db80d9de64051
#App Secret
#    c822c95e9c5218a848dc9d774b246f3e
#URL
#    http://localhost/
#Support email
#    fb@salesking.de
#Support URL
#    http://www.homemadebodycleanse.com
#
#Canvas URL
#    http://localhost/myapp/test/
#Canvas Page
#    myapp
