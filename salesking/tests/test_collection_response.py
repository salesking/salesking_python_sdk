from salesking.tests.base import SalesKingBaseTestCase
from salesking import collection


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
        items = col.get_items()
        self.assertTrue(len(items) > 0)
        self.assertTrue(col.total_pages >= 1)
        self.assertTrue(col.total_entries > 0)
        

