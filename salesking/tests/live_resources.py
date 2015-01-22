from salesking.tests.base import SalesKingBaseTestCase
from salesking.tests.resources import ResourceBaseTestCase
from salesking import api, resources, collection


class ResourceFactoryTestCase(ResourceBaseTestCase):
    
    def test_contact_resource_save_and_delete_success(self):
        clnt = api.APIClient()
        model = resources.get_model_class("contact", api=clnt)
        client = model(self.valid_data)
        msg = u"data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data()) > 0, msg)
        client = client.save()
        self.assertTrue(client.get_id() is not None)
        response = client.delete()
        self.assertEquals(response.status_code, 200)

    def test_contact_add_address_embedded_save_success(self):
        model = resources.get_model_class("contact")
        client = model(self.valid_data)
        model = resources.get_model_class("address")
        address = model()
        address.city = u"Duisburg"
        address.address1 = u"Foo Street"
        address.address2 = u"Appartment Bar"
        address.address_type = u"work"
        msg = "data is: %s" % (address.get_data())
        self.assertTrue(len(address.get_data()) >0, msg)
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data()) >0, msg)
        client.addresses = [address]
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(client.get_data().find(u"Duisburg") >0, msg)
        client = client.save()
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(client.get_data().find(u"Duisburg") >0, msg)
        self.assertTrue(client.id is not None ,msg)
        
    
        
        