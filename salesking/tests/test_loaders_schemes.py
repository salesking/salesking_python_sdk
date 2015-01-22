from os import listdir
from os.path import isfile, join

from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection
from salesking.exceptions import SalesKingException,APIException
from mock import Mock
    
    
class TestLoadersSchemesCase(SalesKingBaseTestCase):

    def setUp(self):
        super(TestLoadersSchemesCase,self).setUp()
        self.api_client = api.APIClient()
        
    def test_initialize_all_json_schemes_as_collections(self):
        all_file_names = self._load_all_filenames_from_disk()
        all_files_cnt = len(all_file_names)
        for afile in all_file_names:
            schema_name = afile.split(".")
            col = None
            try:
                col = collection.get_collection_instance(schema_name[0])
                #print "successfully initialized %s" % schema_name[0]
            except APIException:
                print "no list endpoint %s" % schema_name[0]
            except:
                print "failed as collection %s" % schema_name[0]
                raise 
            col.set_per_page(10)
            col.load()
        self.assertTrue(True)
    
    def test_initialize_all_json_schemes_as_models(self):
        all_file_names = self._load_all_filenames_from_disk()
        all_files_cnt = len(all_file_names)
        for afile in all_file_names:
            schema_name = afile.split(".")
            try:
                model = resources.get_model_class(schema_name[0])
            except:
                print "failed as model %s" % schema_name[0]
                raise
        self.assertTrue(True)
    
    
    def _load_all_filenames_from_disk(self):
        from salesking.conf.settings import SCHEMA_ROOT
        all_files = [ f for f in listdir(SCHEMA_ROOT) if isfile(join(SCHEMA_ROOT,f)) ]
        return all_files