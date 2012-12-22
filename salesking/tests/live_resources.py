from salesking.tests.base import SalesKingBaseTestCase
from salesking.tests.resources import ResourceBaseTestCase
from salesking import api, resources, collection

class ResourceFactoryTestCase(ResourceBaseTestCase):
    
    def test_client_resource_save_and_delete_success(self):
        clnt = api.APIClient()
        model = resources.get_model_class("client",api=clnt)
        client = model(self.valid_data)
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(len(client.get_data())>0,msg)
        client = client.save()
        self.assertTrue(client.get_id() is not None)
        response = client.delete()
        self.assertEquals(response.status_code,200)
        
    def test_client_add_address_embedded_save_and_delete_success(self):
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
        client = client.save()
        msg = "data is: %s" % (client.get_data())
        self.assertTrue(client.get_data().find(u"Duisburg")>0,msg)
        self.assertTrue(client.id is not None ,msg)
        #response = client.delete()
        #self.assertEquals(response.status_code,200)
    
    def test_client_collection_lookup_and_delete_all_organisations_named_sk_success(self):
        valid_filters = {"q":"salesking"}
        col=collection.get_collection_instance("client")
        col.set_filters(valid_filters)
        col.load()
        msg = "query:%s" % col._last_query_str
        self.assertTrue(col._last_query_str is not None, msg)
        self.assertTrue(len(col.items) > 0)
        self.assertEquals(col.total_pages,1)
        
        for x in col.items:
            print "numbers %s" % x.number
            x.delete()
        col.load()
        msg = "query:%s" % col._last_query_str
        self.assertTrue(col._last_query_str is not None, msg)
        self.assertEquals(col.total_pages,1)
        self.assertEquals(col.total_entries,0)
        self.assertTrue(len(col.items)==0)
        
        