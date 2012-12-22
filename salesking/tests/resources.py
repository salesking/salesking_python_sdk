from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources

class ResourceBaseTestCase(SalesKingBaseTestCase):

    valid_data = {'organisation': u"salesking",
                  'last_name': u"Jane",
                  'first_name': u"Dow",
                  'notes': u"APITEST",
                  'email': u"salesking.py-api@mailinator.com"
    }
    
    required_missing_data = {
                  'last_name': u"Jane",
                  'first_name': u"Dow"
    }
    
    class MockResponse(object):
        mock_id = u"a8Ts8KsGar4OMPabxfpGMl"
        mock_number = u"K-2012-012"
        mock_created_at = u"2012-12-19T18:19:25+01:00"
        mock_first_name = u"Dow"
        def __init__(self):
            self.content =u'''
            {"client":
            {"id":"a8Ts8KsGar4OMPabxfpGMl","number":"K-2012-012","organisation":"salesking","last_name":"Jane",
            "first_name":"Dow","gender":null,"notes":null,"position":null,"title":null,"tax_number":null,
            "vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"","created_at":"2012-12-19T18:19:25+01:00",
            "updated_at":"2012-12-19T18:19:25+01:00","language":null,"currency":"EUR","payment_method":null,
            "bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,
            "bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,
            "lock_version":0,"cash_discount":null,"due_days":null,
            "address_field":"salesking","addresses":[],"team_id":null},
            "links":[
                {"rel":"self","href":"clients/a8Ts8KsGar4OMPabxfpGMl"},
                {"rel":"instances","href":"clients"},{"rel":"destroy","href":"clients/a8Ts8KsGar4OMPabxfpGMl"},
                {"rel":"update","href":"clients/a8Ts8KsGar4OMPabxfpGMl"},
                {"rel":"create","href":"clients"},
                {"rel":"documents","href":"clients/a8Ts8KsGar4OMPabxfpGMl/documents"},
                {"rel":"attachments","href":"clients/a8Ts8KsGar4OMPabxfpGMl/attachments"},
                {"rel":"invoices","href":"clients/a8Ts8KsGar4OMPabxfpGMl/invoices"},
                {"rel":"estimates","href":"clients/a8Ts8KsGar4OMPabxfpGMl/estimates"},
                {"rel":"orders","href":"clients/a8Ts8KsGar4OMPabxfpGMl/orders"},
                {"rel":"credit_notes","href":"clients/a8Ts8KsGar4OMPabxfpGMl/credit_notes"},
                {"rel":"recurrings","href":"clients/a8Ts8KsGar4OMPabxfpGMl/recurrings"},
                {"rel":"payment_reminders","href":"clients/a8Ts8KsGar4OMPabxfpGMl/payment_reminders"},
                {"rel":"comments","href":"clients/a8Ts8KsGar4OMPabxfpGMl/comments"},
                {"rel":"emails","href":"clients/a8Ts8KsGar4OMPabxfpGMl/emails"}
            ]
        }
        '''.replace(u"\n",u"").replace(u"\t",u"").replace(u" ",u"")
    mock_response = MockResponse()

class ResourceFactoryTestCase(ResourceBaseTestCase):
        
    def test_initialize_client_resource_success(self):
        model = resources.get_model_class("client")
        client = model(self.valid_data)
        self.assertEquals(client.__class__.__name__,u'client')
        self.assertEquals(client.organisation,u'salesking')
        self.assertEquals(client.first_name,u"Dow")
        #autoinitialize ? 
        self.assertFalse(client.__api__ is None)
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data())>0,msg)
        client.first_name = u"honey"
        self.assertEquals(client.first_name,u"honey")
        client.gender="male"

    def test_initialize_client_required_missing_success(self):
        """
        test schema loading patched required to False
        """
        model = resources.get_model_class("client")
        thrown = False
        try:
            model(self.required_missing_data)
        except ValueError, ex:
            thrown = True
        self.assertFalse(thrown)
        
    def test_initialize_client_empty_success(self):
        model = resources.get_model_class("client")
        thrown = False
        client = None
        try:
            client=model()
        except ValueError, ex:
            thrown = True
        self.assertFalse(thrown)
        
    def test_client_save_response_mock_success(self):
        clnt = api.APIClient()
        model = resources.get_model_class("client",api=clnt)
        client = model(self.valid_data)
        self.assertEquals(client.__class__.__name__,u'client')
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data())>0,msg)
        ### mock the save response ###
        response = self.mock_response
        obj = client.get_object_from_response(response)
        self.assertEquals(obj.__class__.__name__,u'client')
        self.assertEquals(obj.first_name, response.mock_first_name)
        self.assertEquals(obj.number, response.mock_number)
        self.assertEquals(obj.get_id(), response.mock_id)
        self.assertEquals(obj.id, response.mock_id)
        obj.last_name = u"lasst"
        self.assertEquals(obj.last_name, u"lasst")

    def test_client_add_address(self):
        model = resources.get_model_class("client")
        client = model(self.valid_data)
        model = resources.get_model_class("address")
        address = model()
        address.city = u"Duisburg"
        address.address1 = u"Foo Street"
        address.address2 = u"Appartment Bar"
        address.address_type = u"work"
        msg = "data is: %s" % (address.get_data())
        self.assertTrue(len(address.get_data())>0,msg)
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data())>0,msg)
        client.addresses = [address]
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(client.get_data().find(u"Duisburg")>0,msg)
        
         
#    def test_client_resource_schema_get_success(self):
#        clnt = api.APIClient()
#        model = resources.get_model_class("client",api=clnt)
#        client = model(self.valid_data)
#        resp = client.get_resource_remote_schema()
#        msg ="body:%s" % (resp.content)
#        self.assertEquals(resp.status_code, 200, msg)
        
