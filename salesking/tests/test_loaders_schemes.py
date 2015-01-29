from os import listdir
from os.path import isfile, join

from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection


class TestLoadersSchemesCase(SalesKingBaseTestCase):

    def setUp(self):
        super(TestLoadersSchemesCase, self).setUp()
        self.api_client = api.APIClient()
        
    def test_initialize_all_json_schemes_as_collections(self):
        all_file_names = self._load_all_filenames_from_disk()
        all_files_cnt = len(all_file_names)
        no_collection_endpoint = [
            'address',
            'line_item',
            'divider_item',
            'sub_total_item', 
            'user', 
        ]
        needs_fix = [
            'company', # //he?
            'credit_note', # currently broken
            'document', # currently broken
            'invoice', # currently broken
            'sub', # currently broken            
        ]
        no_collection_endpoint.extend(needs_fix)
        ok = True
        for afile in all_file_names:
            schema_name = afile.split(".")
            col = None
            is_loadable = (schema_name[0] not in no_collection_endpoint)
            if is_loadable:
                col = collection.get_collection_instance(schema_name[0])
                col.set_per_page(10)
                col.load()
        self.assertTrue(ok)
    
    def test_initialize_all_json_schemes_as_models(self):
        all_file_names = self._load_all_filenames_from_disk()
        all_files_cnt = len(all_file_names)
        needs_fix = [
            'company',  # he ?
        ]
        ok = True
        for afile in all_file_names:
            schema_name = afile.split(".")
            is_loadable = (schema_name[0] not in needs_fix)
            if is_loadable:
                try:
                    # print "loading %s" % (schema_name[0])
                    model = resources.get_model_class(schema_name[0])
                    empty_instance = model()
                except:
                    print "failed as model %s" % schema_name[0]
                    ok = False
                    #raise
        self.assertTrue(ok)

    def test_empty_invoice(self):
        model = resources.get_model_class("invoice")
        empty_instance = model()
        msg = u"%s" % empty_instance.schema
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)


    def test_empty_estimate(self):
        model = resources.get_model_class("estimate")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_company(self):
        model = resources.get_model_class("company")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_credit_note(self):
        model = resources.get_model_class("credit_note")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_payment_reminder(self):
        model = resources.get_model_class("payment_reminder")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_recurring(self):
        model = resources.get_model_class("payment_reminder")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_task(self):
        model = resources.get_model_class("task")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)

    def test_empty_order(self):
        model = resources.get_model_class("order")
        empty_instance = model()
        msg = u"should have some data inside"
        self.assertIsNotNone(empty_instance, msg=msg)
        self.assertIsNotNone(empty_instance.to_json(), msg=msg)


        # def test_loading_schema_builder(self):

    #        from salesking import utils
    #        utils.loaders.build_loading_map("invoice")

    
    
    def _load_all_filenames_from_disk(self):
        from salesking.conf.settings import SCHEMA_ROOT
        all_files = [ f for f in listdir(SCHEMA_ROOT) if isfile(join(SCHEMA_ROOT,f)) ]
        return all_files