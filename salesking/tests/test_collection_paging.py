from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection
from salesking.exceptions import SalesKingException
from mock import Mock
    
    
class LiveCollectionBaseTestCase(SalesKingBaseTestCase):

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
        
        super(LiveCollectionBaseTestCase,self).setUp()
        self.api_client = api.APIClient()
        # check if we need to setup 21 sk-clients
        valid_filters = {"organisation": self.org_name_token}
        col = collection.get_collection_instance("contact")
        col.set_filters(valid_filters)
        # executes the query
        col.load()
        items_per_page_cnt = col.get_per_page()
        self.total_pages = col.get_total_pages()
        total_entries = col.get_total_entries()
        current_page = col.get_current_page()
        msg = "filters:%s,\nper page cnt %s, total pages %s, total entries %s, current_page %s" % (
               valid_filters,items_per_page_cnt,self.total_pages,total_entries, current_page)
        #print msg
        if total_entries <= 21:
            # create 21 clients
            model = resources.get_model_class("contact", api=self.api_client)
            for x in xrange (total_entries, 21):
                self.valid_data["organisation"] = "%s%s" % (self.org_name_token, x)
                client = model(self.valid_data)
                client = client.save()
        
    def test_get_a_contacts_collection_and_page_to_last_page_items_are_different(self):
        valid_filters = {u"organisation": self.org_name_token}
        col = collection.get_collection_instance("contact")
        col.set_filters(valid_filters)
        col.set_per_page(10)
        col.load()
        page_1_url = col._last_query_str
        
        #see setup
        self.assertTrue(col.get_total_entries()>=21)
        self.assertTrue(len(col.get_items()) == col.get_per_page())
        self.assertTrue(col.get_total_pages() > 2)
        
        first_page_ids = []
        items = col.get_items()
        for x in range(0,len(items)):
            obj = items[x].number
            first_page_ids.append(obj)
        self.assertEquals(len(first_page_ids), 10)
        #print first_page_ids
        col.clear_items()
        col.load(page = col.get_total_pages())
        page_2_url = col._last_query_str
        msg = u"%s\n%s\n should not be equal" % (page_1_url, page_2_url)
        self.assertNotEquals(page_1_url, page_2_url, msg)
        last_item = col.get_items()[0]
        last_number = last_item.number
        print last_number
        self.assertTrue(len(last_number) > 0)
        self.assertTrue(last_number not in first_page_ids)
        
    def test_other_then_startpage(self):
        valid_filters = {u"organisation": self.org_name_token}
        col = collection.get_collection_instance("contact")
        col.set_filters(valid_filters)
        col.set_per_page(10)
        col.load(page=self.total_pages)
        page_1_url = col._last_query_str
        
        #see setup
        self.assertTrue(col.get_total_entries()>=21)
        self.assertTrue(len(col.get_items()) == col.get_per_page())
        self.assertTrue(col.get_total_pages() > 2)
        
        first_page_ids = []
        items = col.get_items()
        for x in range(0,len(items)):
            obj = items[x].number
            first_page_ids.append(obj)
        self.assertEquals(len(first_page_ids), 10)
        