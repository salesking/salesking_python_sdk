from salesking.tests.base import SalesKingBaseTestCase
from salesking import api


class TestLoadersSchemesCase(SalesKingBaseTestCase):
    def setUp(self):
        super(TestLoadersSchemesCase, self).setUp()
        self.api_client = api.APIClient()
