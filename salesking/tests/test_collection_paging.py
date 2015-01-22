from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection
from salesking.exceptions import SalesKingException
from mock import Mock
    
    
class LiveCollectionBaseTestCase(SalesKingBaseTestCase):

    valid_data = {'organisation': u"fb-",
                  'last_name': u"JaneColl",
                  'first_name': u"DowColl",
                  'notes': u"APITEST-Collection-Testcase",
                  'email': u"salesking.py-api@mailinator.com"
    }
    
    org_name_token = u"fb-"

    def setUp(self):
        """
        this test is slow as it gets over the air
        creates 201 resources of client named fb-counter
        if they do not exist
        """
        
        super(LiveCollectionBaseTestCase,self).setUp()
        self.api_client = api.APIClient()
        # check if we need to setup 201 sk-clients
        valid_filters = {"q": self.org_name_token}
        col = collection.get_collection_instance("client")
        col.set_filters(valid_filters)
        # executes the query
        col.load()
        items_per_page_cnt = col.get_per_page()
        total_pages = col.get_total_pages()
        total_entries = col.get_total_entries()
        current_page = col.get_current_page()
        msg = "filters:%s,\nper page cnt %s, total pages %s, total entries %s, current_page %s" % (
               valid_filters,items_per_page_cnt,total_pages,total_entries, current_page)
        #print msg
        if total_entries <= 201:
            # create 201 clients
            model = resources.get_model_class("client", api=self.api_client)
            for x in xrange (total_entries, 201):
                self.valid_data["organisation"] = "%s%s" % (self.org_name_token,x)
                client = model(self.valid_data)
                client = client.save()
        
    def test_get_a_collection_page_to_next(self):
        valid_filters = {u"organisation": self.org_name_token}
        col=collection.get_collection_instance("client")
        col.set_filters(valid_filters)
        # executes the query
        col.load()
        self.assertEquals(col.get_total_entries(),201)
        
    
