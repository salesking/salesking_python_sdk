from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, collection


class LiveInvoiceCollectionBaseTestCase(SalesKingBaseTestCase):

    valid_data = {'organisation': u"fb-",
                  'last_name': u"JaneColl",
                  'first_name': u"DowColl",
                  'notes': u"APITEST-Collection LiveCollectionBaseTestCase",
                  'email': u"sking.py-api@mailinator.com"
    }
    
    org_name_token = u"fb-"

    def setUp(self):
        """
        this test is slow as it gets over the air
        creates 201 resources of client named fb-counter
        if they do not exist
        """
        
        super(LiveInvoiceCollectionBaseTestCase,self).setUp()
        self.api_client = api.APIClient()
        
    def test_get_invoice_collection(self):
        valid_filters = {u"q": self.org_name_token}
        col = collection.get_collection_instance("invoice")
        col.set_filters(valid_filters)
        col.set_per_page(10)
        col.load()
        page_1_url = col._last_query_str
        items = col.get_items()
        #see setup
        self.assertTrue(col.get_total_pages() > 0)
        