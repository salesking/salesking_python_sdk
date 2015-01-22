from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection
from salesking.exceptions import SalesKingException
from mock import Mock
    
    
class LiveCollectionResponseTestCase(SalesKingBaseTestCase):

    
    def test_contact_collection_to_valid_items_success(self):
        """
        Assumes there is already a Client created manually
        """
        valid_filters = {"organisation": "salesking", "type": "Client"}
        col = collection.get_collection_instance("contact")
        col.set_filters(valid_filters)
        col.load()
        msg = "query:%s" % col._last_query_str
        self.assertTrue(col._last_query_str is not None, msg)
        self.assertTrue(len(col.get_items()) > 0)
        self.assertTrue(col.total_pages >= 1)
        self.assertTrue(col.total_entries > 0)
        

