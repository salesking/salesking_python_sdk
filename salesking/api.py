#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
try:
    import simplejson as json
except ImportError:
    import json
    
from urllib import urlencode
import requests
from oauth_hook import OAuthHook
    
from salesking.conf import settings
from salesking import exceptions 


log = logging.getLogger(__name__)


class SalesKingApiBase(object):
    def __init__(self):
        self.app_id = settings.API['app_id']
        self.app_secret = settings.API['app_secret']
        self.oauth_redirect_url = settings.API['oauth_redirect_url']
        self.app_scope = settings.API['app_scope']
        self.base_url = settings.API['base_url']%(settings.API['sk_subdomain'])
        self.sk_user = settings.API['sk_user']
        self.sk_pw = settings.API['sk_pw']
        # use oauth only if basic auth is not possible
        self.use_oauth = (self.sk_user is None or self.sk_pw is None) 
        self.access_token_url = u"%s%s" % (self.base_url,settings.ACCESS_TOKEN_URL)
        self.client = None
        if self.use_oauth:
            OAuthHook.consumer_key = consumer_key
            OAuthHook.consumer_secret = consumer_secret
            self.oauth_hook = OAuthHook(access_token, access_token_secret, header_auth=True)
            
        if self.app_id is None or len(self.app_id)==0:
            raise Exception("please configure your sdk in salesking.conf.local_settings")
            
      
    def _get_authorization_url(self,scope=False):
        params = {
                  u"client_id": self.app_id,
                  u"scope": scope if scope else self.app_scope,
                  u"redirect_uri": self.redirect_url
        }
        return u"%s?%s" %(self.auth_url,urlencode(params))
    
    def _get_access_token_url(self,code):
        params = {
                  u"client_id": self.app_id,
                  u"client_secret": self.app_secret,
                  u"redirect_uri": self.oauth_redirect_url,
                  u"code": code
        }
        return u"%s?%s" %(self.access_token_url,urlencode(params))

    def request(self, url, method = u"get", data = None, headers = None, **kwargs):
        """
        public method for doing the live request
        """

        url, method, data, headers, kwargs = self._pre_request(url, 
                                                                 method=method,
                                                                 data=data,
                                                                 headers=headers,
                                                                 **kwargs)
        response = self._request(url, method=method, data=data, headers=headers, **kwargs)
        response = self._post_request(response)
        response = self._handle_response(response)
        
        return response

    def _pre_request(self, url, method = u"get", data = None, headers=None, **kwargs):
        """
        hook for manipulating the _pre request data
        """
        return (url, method, data, headers, kwargs)

    def _request(self, url, method = u"get", data = None, headers=None, **kwargs):
        raise Exception("_request needs to be implemented in subclass")


    def _post_request(self, response):
        """
        hook for post request handling
        """
        #print "response.content:%s" % (response.content)
        return response    
    
    def _handle_response(self,response):
        """
        hook for hanlding the response
        """
        return response

    def _de_hydrate(self,response):
        log.debug("response: %s" % response.text)
        return json.loads(response.text)
    
    def request_access_token(self,code):
        url = self._get_access_token_url(code)
        r = self.request(url)
        if r.status_code == 200 and r.text.find(u"error")==-1:
            return self._de_hydrate(r)
        raise exceptions.SalesKingException("REQUESTTOKEN_ERROR","Could not fetch access_token",r)


class APIClient(SalesKingApiBase):    
    access_token = None
    
    def _pre_request(self, url, method = u"get", data = None, headers=None, **kwargs):
        """
        hook for manipulating the _pre request data
        """
        header = {
            u"Content-Type": u"application/json",
            u"User-Agent": u"salesking_api_py_v1",
        }
        if headers:
            headers.update(header)
        else:
            headers = header
        if url.find(self.base_url) !=0:
            url = u"%s%s" %(self.base_url, url)
        return (url, method, data, headers, kwargs)

    def _request(self, url, method = u"get", data = None, headers=None, **kwargs):
        """
        does the request via requests
        - oauth not implemented yet
        - use basic auth please
        """
        #        if self.access_token:
        #            auth_header = {
        #                u"Authorization": "Bearer %s" % (self.access_token)
        #            }
        #            headers.update(auth_header)
        #basic auth
        msg = "method: %s url:%s\nheaders:%s\ndata:%s" % (
                   method,url,headers,data)
        #print msg
        if not self.use_oauth:
            auth=(self.sk_user, self.sk_pw)
            if not self.client:
                self.client = requests.session()
            r = self.client.request(method, url, headers=headers, data=data, auth=auth,**kwargs)
        else:
            if not self.client:
                self.client = requests.session(hooks={'pre_request': oauth_hook})
            r = self.client.request(method, url, headers=headers, data=data,**kwargs)
        return r
    
    def _handle_response(self,response):
        status = response.status_code
        if status == 400:
          raise exceptions.BadRequest(response)
        elif status == 401:
          raise exceptions.Unauthorized(response)
        elif status == 404:
          raise exceptions.NotFound()
        elif status == 422:
          raise exceptions.BadRequest(response)
        elif status in range(400, 500):
          raise exceptions.HttpClientError("Client Error %s: " % (response.status_code), response=response, content=response.content)
        elif status in range(500, 600):
          raise exceptions.ServerError()
        return response
