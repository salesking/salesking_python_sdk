from salesking.tests.base import SalesKingBaseTestCase
from salesking.tests.resources import ResourceBaseTestCase
from salesking import api, resources

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