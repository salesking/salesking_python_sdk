from salesking import api, resources, collection
from salesking import exceptions

from salesking.tests.base import SalesKingBaseTestCase
from salesking.tests.resources import ResourceBaseTestCase


class MockResponse(object):
        
        def __init__(self, status_code):
            self.status_code = status_code
            self.content = u"foo content"


class ResponseExceptionsTestCase(ResourceBaseTestCase):
    
    def test_live_404_exception_thrown(self):
        clnt = api.APIClient()
        model = resources.get_model_class("client", api=clnt)
        client = model(self.valid_data)
        client.__api__.base_url += "foo"
        
        with self.assertRaises(exceptions.NotFound):
            client = client.save()
        
    
    def test_400_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.BadRequest):
            res = clnt._handle_response(MockResponse(400))
    
    def test_401_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.Unauthorized):
            res = clnt._handle_response(MockResponse(401))
    
    def test_404_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.NotFound):
            res = clnt._handle_response(MockResponse(404))
    
    def test_408_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.BadRequest):
            res = clnt._handle_response(MockResponse(408))
    
    def test_422_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.BadRequest):
            res = clnt._handle_response(MockResponse(422))
    
    def test_555_fake_exception(self):
        clnt = api.APIClient()
        with self.assertRaises(exceptions.ServerError):
            res = clnt._handle_response(MockResponse(555))
        
    