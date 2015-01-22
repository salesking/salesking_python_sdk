from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources, collection
from salesking.exceptions import SalesKingException
from mock import Mock
    
    
class CollectionBaseTestCase(SalesKingBaseTestCase):
    
    class MockCollectionResponse(object):
        
        def __init__(self):
            self.status_code = 200
            self.content =u'''
            {"contacts":[
                {"contact":
                    {"id":"a2Ux6yswWr4RHCabxfpGMl","number":"K-2012-001","organisation":"salesking123","last_name":"Jane",
                    "first_name":"Dow","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,
                    "email":"","url":null,"birthday":null,"tag_list":"","created_at":"2012-12-19T00:39:49+01:00",
                    "updated_at":"2012-12-19T00:39:49+01:00","language":null,"currency":"EUR",
                    "payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,
                    "bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,
                    "lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking123",
                    "addresses":[],"team_id":null
                    },
                    "links":[
                        {"rel":"self","href":"contacts/a2Ux6yswWr4RHCabxfpGMl"},{"rel":"instances","href":"contacts"},
                        {"rel":"destroy","href":"contacts/a2Ux6yswWr4RHCabxfpGMl"},{"rel":"update","href":"contacts/a2Ux6yswWr4RHCabxfpGMl"},
                        {"rel":"create","href":"contacts"},{"rel":"documents","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/documents"},
                        {"rel":"attachments","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/attachments"},
                        {"rel":"invoices","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/invoices"},
                        {"rel":"estimates","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/estimates"},
                        {"rel":"orders","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/orders"},
                        {"rel":"credit_notes","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/credit_notes"},
                        {"rel":"recurrings","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/recurrings"},
                        {"rel":"payment_reminders","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/payment_reminders"},
                        {"rel":"comments","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/comments"},
                        {"rel":"emails","href":"contacts/a2Ux6yswWr4RHCabxfpGMl/emails"}
                        ]
                    },
                {"contact":
                    {"id":"a4G5EUsD8r4PJgabxfpGMl","number":"K-2012-008","organisation":"king","last_name":"schnarz","first_name":"Hans",
                    "gender":null,"notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,
                    "birthday":null,"tag_list":"","created_at":"2012-12-19T14:23:04+01:00","updated_at":"2012-12-19T14:23:04+01:00",
                    "language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,
                    "bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,
                    "phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,
                    "address_field":"king","addresses":[],"team_id":null
                    },
                    "links":
                        [{"rel":"self","href":"contacts/a4G5EUsD8r4PJgabxfpGMl"},{"rel":"instances","href":"contacts"},
                        {"rel":"destroy","href":"contacts/a4G5EUsD8r4PJgabxfpGMl"},{"rel":"update","href":"contacts/a4G5EUsD8r4PJgabxfpGMl"},
                        {"rel":"create","href":"contacts"},{"rel":"documents","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/documents"},
                        {"rel":"attachments","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/attachments"},
                        {"rel":"invoices","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/invoices"},
                        {"rel":"estimates","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/estimates"},
                        {"rel":"orders","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/orders"},
                        {"rel":"credit_notes","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/credit_notes"},
                        {"rel":"recurrings","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/recurrings"},
                        {"rel":"payment_reminders","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/payment_reminders"},
                        {"rel":"comments","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/comments"},
                        {"rel":"emails","href":"contacts/a4G5EUsD8r4PJgabxfpGMl/emails"}]},
                {"contact":{"id":"a6N570lb8r4yBvabxfpGMl","number":"K-01012-911","organisation":"Funky Music Times","last_name":"Darwin","first_name":"George","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"",
                 "url":null,"birthday":null,"tag_list":"!example","created_at":"2011-12-21T23:00:43+01:00","updated_at":"2012-02-02T20:06:01+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":1,"cash_discount":null,"due_days":null,"address_field":"Funky Music Times\n71 Brushfield St\nE1 6 Greater London","addresses":[{"address":{"id":"a6N4dclb8r4yBvabxfpGMl","city":"Greater London","address1":"71 Brushfield St","address2":null,"pobox":"","zip":"E1 6","state":null,"country":null,"created_at":"2011-12-21T23:00:43+01:00","updated_at":"2011-12-21T23:00:43+01:00","address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}}],"team_id":null},"links":[{"rel":"self","href":"contacts/a6N570lb8r4yBvabxfpGMl"},{"rel":"instances","href":"contacts"},{"rel":"destroy","href":"contacts/a6N570lb8r4yBvabxfpGMl"},{"rel":"update","href":"contacts/a6N570lb8r4yBvabxfpGMl"},{"rel":"create","href":"contacts"},{"rel":"documents","href":"contacts/a6N570lb8r4yBvabxfpGMl/documents"},{"rel":"attachments","href":"contacts/a6N570lb8r4yBvabxfpGMl/attachments"},{"rel":"invoices","href":"contacts/a6N570lb8r4yBvabxfpGMl/invoices"},{"rel":"estimates","href":"contacts/a6N570lb8r4yBvabxfpGMl/estimates"},{"rel":"orders","href":"contacts/a6N570lb8r4yBvabxfpGMl/orders"},{"rel":"credit_notes","href":"contacts/a6N570lb8r4yBvabxfpGMl/credit_notes"},{"rel":"recurrings","href":"contacts/a6N570lb8r4yBvabxfpGMl/recurrings"},{"rel":"payment_reminders","href":"contacts/a6N570lb8r4yBvabxfpGMl/payment_reminders"},{"rel":"comments","href":"contacts/a6N570lb8r4yBvabxfpGMl/comments"},{"rel":"emails","href":"contacts/a6N570lb8r4yBvabxfpGMl/emails"}]},
                 {"contact":{"id":"bUvvUglb4r4BelabxfpGMl","number":"K-01012-728","organisation":"Werbeagentur Gl\u00fcck","last_name":"zu Fall","first_name":"Rainer","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"!example","created_at":"2011-12-21T22:55:00+01:00","updated_at":"2012-02-02T20:07:36+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":1,"cash_discount":null,"due_days":null,"address_field":"Werbeagentur Gl\u00fcck\nKleeweg 4\n30001 Berlin","addresses":[{"address":{"id":"bUvub0lb4r4BelabxfpGMl","city":"Berlin","address1":"Kleeweg 4","address2":null,"pobox":"","zip":"30001","state":null,"country":null,"created_at":"2011-12-21T22:55:00+01:00","updated_at":"2011-12-21T22:55:00+01:00","address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}}],"team_id":null},"links":[{"rel":"self","href":"contacts/bUvvUglb4r4BelabxfpGMl"},{"rel":"instances","href":"contacts"},{"rel":"destroy","href":"contacts/bUvvUglb4r4BelabxfpGMl"},{"rel":"update","href":"contacts/bUvvUglb4r4BelabxfpGMl"},{"rel":"create","href":"contacts"},{"rel":"documents","href":"contacts/bUvvUglb4r4BelabxfpGMl/documents"},{"rel":"attachments","href":"contacts/bUvvUglb4r4BelabxfpGMl/attachments"},{"rel":"invoices","href":"contacts/bUvvUglb4r4BelabxfpGMl/invoices"},{"rel":"estimates","href":"contacts/bUvvUglb4r4BelabxfpGMl/estimates"},{"rel":"orders","href":"contacts/bUvvUglb4r4BelabxfpGMl/orders"},{"rel":"credit_notes","href":"contacts/bUvvUglb4r4BelabxfpGMl/credit_notes"},{"rel":"recurrings","href":"contacts/bUvvUglb4r4BelabxfpGMl/recurrings"},{"rel":"payment_reminders","href":"contacts/bUvvUglb4r4BelabxfpGMl/payment_reminders"},{"rel":"comments","href":"contacts/bUvvUglb4r4BelabxfpGMl/comments"},{"rel":"emails","href":"contacts/bUvvUglb4r4BelabxfpGMl/emails"}]},
                 {"contact":{"id":"dzYOHCswWr4RopabxfpGMl","number":"K-2012-002","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"","created_at":"2012-12-19T00:44:23+01:00","updated_at":"2012-12-19T00:44:23+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking","addresses":[],"team_id":null},"links":[{"rel":"self","href":"contacts/dzYOHCswWr4RopabxfpGMl"},{"rel":"instances","href":"contacts"},{"rel":"destroy","href":"contacts/dzYOHCswWr4RopabxfpGMl"},{"rel":"update","href":"contacts/dzYOHCswWr4RopabxfpGMl"},{"rel":"create","href":"contacts"},{"rel":"documents","href":"contacts/dzYOHCswWr4RopabxfpGMl/documents"},{"rel":"attachments","href":"contacts/dzYOHCswWr4RopabxfpGMl/attachments"},{"rel":"invoices","href":"contacts/dzYOHCswWr4RopabxfpGMl/invoices"},{"rel":"estimates","href":"contacts/dzYOHCswWr4RopabxfpGMl/estimates"},{"rel":"orders","href":"contacts/dzYOHCswWr4RopabxfpGMl/orders"},{"rel":"credit_notes","href":"contacts/dzYOHCswWr4RopabxfpGMl/credit_notes"},{"rel":"recurrings","href":"contacts/dzYOHCswWr4RopabxfpGMl/recurrings"},{"rel":"payment_reminders","href":"contacts/dzYOHCswWr4RopabxfpGMl/payment_reminders"},{"rel":"comments","href":"contacts/dzYOHCswWr4RopabxfpGMl/comments"},
                 {"rel":"emails","href":"contacts/dzYOHCswWr4RopabxfpGMl/emails"}]}
                 ],
                "links":{"next":"https://frank.dev.salesking.eu/api/contacts?page=2","self":"https://frank.dev.salesking.eu/api/contacts?page=1"},
                "collection":{"current_page":1,"per_page":50,"total_entries":5,"total_pages":1}
                }'''.replace(u"\n",u"").replace(u"\t",u"")
    mock_response = MockCollectionResponse()



class CollectionTestCase(CollectionBaseTestCase):

    coll = None
    # mock the salesking api having a get request
    # mocking the saleskingcolleciont config
    def setUp(self):
        self.api_client = api.APIClient()
        self.api_mock = Mock()
        self.api_mock.request.return_value = self.mock_response

    def test_initialise_collection(self):
        col=collection.get_collection_instance("contact",self.api_mock)
        col.load(page=1)
        self.assertTrue(len(col.items) == 5)
        self.assertEquals(col.items[0].number,u"K-2012-001")
        self.assertEquals(col.items[1].organisation,u"king")
        self.assertEquals(col.items[3].organisation,u"Werbeagentur Gl\u00fcck")
        
    def test_validate_filters(self):
        col=collection.get_collection_instance("contact",self.api_mock)
        #date-time germany
        #self.assertTrue(col.validate_filter("created_at_from","2012-12-19T00:39:49+01:00"));
        self.assertTrue(col.validate_filter("number","string"))
        self.assertFalse(col.validate_filter("notexisting","string"))
        self.assertTrue(col.validate_filter("birthday_to","2012-01-01"));
        self.assertFalse(col.validate_filter("birthday_to","string"));
        self.assertFalse(col.validate_filter("birthday_to","1999-01-32"));
        self.assertFalse(col.validate_filter("birthday_to","1999-13-01"));
        self.assertTrue(col.validate_filter("birthday_to","1999-01-01"));
        self.assertTrue(col.validate_filter("organisation","1999-01-01"));
    
    def test_set_filters(self):
        valid_filters = {"q":"salesking", "number":"K-123-0001"}
        col=collection.get_collection_instance("contact",self.api_mock)
        col.set_filters(valid_filters)
        self.assertEquals(valid_filters, col.get_filters())
        
    def test_add_filters(self):
        col=collection.get_collection_instance("contact",self.api_mock)
        self.assertTrue(col.add_filter("number","astrstring"))
        self.failUnlessRaises(SalesKingException,col.add_filter,"notexisting","string")
    
