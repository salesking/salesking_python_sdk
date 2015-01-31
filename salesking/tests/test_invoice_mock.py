from salesking.tests.base import SalesKingBaseTestCase
from salesking import api, resources


class MockInvoiceResponse(object):
    def __init__(self):
        self.status_code = 200
        self.content = u'''
            {"invoice":
  {"id":"bUAr_Qlb4r4BelabxfpGMl","number":"R-069-2011-215a","address_field":"Werbeagentur Gl\u00fcck\nKleeweg 4\n30001 Berlin","date":"2011-12-21","due_days":3,"due_date":"2011-12-24","status":"closed","external_ref":null,"payment_method":null,"title":"Projekt Tippspiel","notes_before":"Wir m\u00f6chten Ihnen folgende Positionen in Rechnung stellen:","notes_after":"Bitte \u00fcberweisen Sie den Rechnungsbetrag bis zum 24.12.2011.","tag_list":"!example","language":null,"currency":"EUR","exchange_rate":null,"gross_total_exchanged":1950.0,"archived_pdf":
  {"attachment":{"id":"bVKYQ-lb4r4BelabxfpGMl","filename":"just_a_test.pdf","disk_filename":"111221215503038_just_a_test.pdf","url":"https://sk2-dev.s3.amazonaws.com/cPUdkOlb0r4BelabxfpGMl/attachments/Document/111221215503038_just_a_test.pdf?X-Amz-Expires=1200&X-Amz-Date=20150128T181758Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=134E61V8BNTFFTK4T982/20150128/us-east-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=6bcef58961133d4e28963f9e0643751cdaaa6d5a57505c4dd00df69de8628cfe","related_object_type":"Document","related_object_id":"bUAr_Qlb4r4BelabxfpGMl","content_type":"application/pdf","size":32814,"is_signed":null,"created_at":"2011-12-21T22:55:03+01:00","team_id":null},"links":
    [{"rel":"self","href":"attachments/bVKYQ-lb4r4BelabxfpGMl"},
     {"rel":"download","href":"attachments/bVKYQ-lb4r4BelabxfpGMl/download"},
     {"rel":"instances","href":"attachments"},
     {"rel":"destroy","href":"attachments/bVKYQ-lb4r4BelabxfpGMl"}]
     },"sepa_mandate_id":null,"sepa_mandate_signed_at":null,"sepa_debit_sequence_type":null,
     "client":{"links":[
              {"rel":"self","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"instances","href":"clients"},
              {"rel":"destroy","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"update","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"create","href":"clients"},
              {"rel":"documents","href":"clients/bUvvUglb4r4BelabxfpGMl/documents"},
              {"rel":"attachments","href":"clients/bUvvUglb4r4BelabxfpGMl/attachments"},
              {"rel":"invoices","href":"clients/bUvvUglb4r4BelabxfpGMl/invoices"},
              {"rel":"estimates","href":"clients/bUvvUglb4r4BelabxfpGMl/estimates"},
              {"rel":"orders","href":"clients/bUvvUglb4r4BelabxfpGMl/orders"},
              {"rel":"credit_notes","href":"clients/bUvvUglb4r4BelabxfpGMl/credit_notes"},
              {"rel":"recurrings","href":"clients/bUvvUglb4r4BelabxfpGMl/recurrings"},
              {"rel":"payment_reminders","href":"clients/bUvvUglb4r4BelabxfpGMl/payment_reminders"},
              {"rel":"comments","href":"clients/bUvvUglb4r4BelabxfpGMl/comments"},
              {"rel":"emails","href":"clients/bUvvUglb4r4BelabxfpGMl/emails"},
              {"rel":"emails create","href":"clients/bUvvUglb4r4BelabxfpGMl/emails"}
              ],
    "client":{
            "id":"bUvvUglb4r4BelabxfpGMl","parent_id":null,
            "type":"Client","is_employee":false,"number":"K-01012-728",
            "organisation":"Werbeagentur Gl\u00fcck","last_name":"zu Fall","first_name":"Rainer",
            "gender":"male",
            "notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,
            "tag_list":"!example","created_at":"2011-12-21T22:55:00+01:00","updated_at":"2012-02-02T20:07:36+01:00",
            "language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,
            "bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,
            "lock_version":1,"cash_discount":null,"due_days":null,
            "address_field":"Werbeagentur Gl\u00fcck\nHerr Rainer zu Fall\nKleeweg 4\n30001 Berlin",
            "addresses":[{"address":
                         {"id":"bUvub0lb4r4BelabxfpGMl","city":"Berlin","address1":"Kleeweg 4","address2":null,"pobox":"","zip":"30001",
                           "state":null,"country":null,"created_at":"2011-12-21T22:55:00+01:00","updated_at":"2011-12-21T22:55:00+01:00",
                           "address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}
            }],
            "team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":null,
            "sales_potential":null,"probability":null,"expected_revenue":null}},
            "client_id":"bUvvUglb4r4BelabxfpGMl",
            "contact":
            {"contact":
            {"id":"bUvvUglb4r4BelabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-01012-728","organisation":"Werbeagentur Gl\u00fcck","last_name":"zu Fall","first_name":"Rainer","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"!example","created_at":"2011-12-21T22:55:00+01:00","updated_at":"2012-02-02T20:07:36+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":1,"cash_discount":null,"due_days":null,"address_field":"Werbeagentur Gl\u00fcck\nHerr Rainer zu Fall\nKleeweg 4\n30001 Berlin","addresses":
            [{"address":
            {"id":"bUvub0lb4r4BelabxfpGMl","city":"Berlin","address1":"Kleeweg 4","address2":null,"pobox":"","zip":"30001","state":null,"country":null,"created_at":"2011-12-21T22:55:00+01:00","updated_at":"2011-12-21T22:55:00+01:00","address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}}],
             "team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":null,"sales_potential":null,"probability":null,"expected_revenue":null},
             "links":[{"rel":"self","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"instances","href":"contacts"},
                      {"rel":"destroy","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"update","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"create","href":"contacts"},
                      {"rel":"documents","href":"contacts/bUvvUglb4r4BelabxfpGMl/documents"},
                      {"rel":"attachments","href":"contacts/bUvvUglb4r4BelabxfpGMl/attachments"},
                      {"rel":"invoices","href":"contacts/bUvvUglb4r4BelabxfpGMl/invoices"},
                      {"rel":"estimates","href":"contacts/bUvvUglb4r4BelabxfpGMl/estimates"},
                      {"rel":"orders","href":"contacts/bUvvUglb4r4BelabxfpGMl/orders"},
                      {"rel":"credit_notes","href":"contacts/bUvvUglb4r4BelabxfpGMl/credit_notes"},
                      {"rel":"recurrings","href":"contacts/bUvvUglb4r4BelabxfpGMl/recurrings"},
                      {"rel":"payment_reminders","href":"contacts/bUvvUglb4r4BelabxfpGMl/payment_reminders"},
                      {"rel":"comments","href":"contacts/bUvvUglb4r4BelabxfpGMl/comments"},
                      {"rel":"emails","href":"contacts/bUvvUglb4r4BelabxfpGMl/emails"},
                      {"rel":"emails create","href":"contacts/bUvvUglb4r4BelabxfpGMl/emails"}]},
            "contact_id":"bUvvUglb4r4BelabxfpGMl","team_id":null,
            "line_items":[{"line_item":
                          {"id":"bUAl2ylb4r4BelabxfpGMl","position":1,"name":"Projektarbeit","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Tage","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}},
                          {"line_item":
                            {"id":"bUAnt0lb4r4BelabxfpGMl","position":2,"name":"Kaffee trinken","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Tassen","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}},
                          {"line_item":
                            {"id":"bUAoPMlb4r4BelabxfpGMl","position":3,"name":"Bugs Programmieren","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Stunden","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}
            }],
            "items":
                [{"line_item":
                    {"id":"bUAl2ylb4r4BelabxfpGMl","position":4,"name":"Projektarbeit","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Tage","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}
                    },
                    {"line_item":
                    {"id":"bUAnt0lb4r4BelabxfpGMl","position":5,"name":"Kaffee trinken","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Tassen","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}},
                {"line_item":
                    {"id":"bUAoPMlb4r4BelabxfpGMl","position":6,"name":"Bugs Programmieren","type":"LineItem","external_ref":null,"description":null,"price_single":650.0,"cost":null,"cost_total":0.0,"gross_margin_total":650.0,"gross_margin_pct":100.0,"net_total":650.0,"gross_total":650.0,"tax":0.0,"discount":0.0,"quantity_unit":"Stunden","quantity":1.0,"product_id":null,"product_from_line_item":null,"created_at":"2011-12-21T22:55:01+01:00","updated_at":"2011-12-21T22:55:01+01:00","_destroy":false}
                }],
           "created_at":"2011-12-21T22:55:01+01:00","updated_at":"2013-01-23T09:56:46+01:00","lock_version":1,"price_total":1950.0,"price_tax":0.0,"gross_total":1950.0,"tax_total":0.0,"net_total":1950.0,"net_total_base":1950.0,"cost_total":0.0,"gross_margin_total":1950.0,"gross_margin_pct":100.0,"recurring_id":null},
           "links":[{"rel":"self","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"instances","href":"invoices"},
                    {"rel":"destroy","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"update","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"create","href":"invoices"},
                    {"rel":"attachments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/attachments"},
                    {"rel":"payments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payments"},
                    {"rel":"payment_reminders","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payment_reminders"},
                    {"rel":"comments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/comments"},
                    {"rel":"emails","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/emails"},
                    {"rel":"emails create","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/emails"},
                    {"rel":"payment create","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payments"},
                    {"rel":"print","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/print"}]
}
'''.replace(u"\n", u"").replace(u"\t", u"").replace(u" ", u"")


class MockInvoiceNoLineItemResponse(object):
    def __init__(self):
        self.status_code = 200
        self.content = u'''
{"invoice":
  {"id":"bUAr_Qlb4r4BelabxfpGMl","number":"R-069-2011-215","address_field":"Werbeagentur Gl\u00fcck\nKleeweg 4\n30001 Berlin","date":"2011-12-21","due_days":3,"due_date":"2011-12-24","status":"closed","external_ref":null,"payment_method":null,"title":"Projekt Tippspiel","notes_before":"Wir m\u00f6chten Ihnen folgende Positionen in Rechnung stellen:","notes_after":"Bitte \u00fcberweisen Sie den Rechnungsbetrag bis zum 24.12.2011.","tag_list":"!example","language":null,"currency":"EUR","exchange_rate":null,"gross_total_exchanged":1950.0,
  "archived_pdf":
    {"attachment":
        {"id":"bVKYQ-lb4r4BelabxfpGMl","filename":"just_a_test.pdf","disk_filename":"111221215503038_just_a_test.pdf","url":"https://sk2-dev.s3.amazonaws.com/cPUdkOlb0r4BelabxfpGMl/attachments/Document/111221215503038_just_a_test.pdf?X-Amz-Expires=1200&X-Amz-Date=20150128T181758Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=134E61V8BNTFFTK4T982/20150128/us-east-1/s3/aws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=6bcef58961133d4e28963f9e0643751cdaaa6d5a57505c4dd00df69de8628cfe","related_object_type":"Document","related_object_id":"bUAr_Qlb4r4BelabxfpGMl","content_type":"application/pdf","size":32814,"is_signed":null,"created_at":"2011-12-21T22:55:03+01:00",
        "team_id":null},
    "links":
        [{"rel":"self","href":"attachments/bVKYQ-lb4r4BelabxfpGMl"},
         {"rel":"download","href":"attachments/bVKYQ-lb4r4BelabxfpGMl/download"},
         {"rel":"instances","href":"attachments"},
         {"rel":"destroy","href":"attachments/bVKYQ-lb4r4BelabxfpGMl"}]
         },
    "sepa_mandate_id":null,"sepa_mandate_signed_at":null,"sepa_debit_sequence_type":null,
     "client":{"links":[
              {"rel":"self","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"instances","href":"clients"},
              {"rel":"destroy","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"update","href":"clients/bUvvUglb4r4BelabxfpGMl"},
              {"rel":"create","href":"clients"},
              {"rel":"documents","href":"clients/bUvvUglb4r4BelabxfpGMl/documents"},
              {"rel":"attachments","href":"clients/bUvvUglb4r4BelabxfpGMl/attachments"},
              {"rel":"invoices","href":"clients/bUvvUglb4r4BelabxfpGMl/invoices"},
              {"rel":"estimates","href":"clients/bUvvUglb4r4BelabxfpGMl/estimates"},
              {"rel":"orders","href":"clients/bUvvUglb4r4BelabxfpGMl/orders"},
              {"rel":"credit_notes","href":"clients/bUvvUglb4r4BelabxfpGMl/credit_notes"},
              {"rel":"recurrings","href":"clients/bUvvUglb4r4BelabxfpGMl/recurrings"},
              {"rel":"payment_reminders","href":"clients/bUvvUglb4r4BelabxfpGMl/payment_reminders"},
              {"rel":"comments","href":"clients/bUvvUglb4r4BelabxfpGMl/comments"},
              {"rel":"emails","href":"clients/bUvvUglb4r4BelabxfpGMl/emails"},
              {"rel":"emails create","href":"clients/bUvvUglb4r4BelabxfpGMl/emails"}
              ],
    "client":{
            "id":"bUvvUglb4r4BelabxfpGMl","parent_id":null,
            "type":"Client","is_employee":false,"number":"K-01012-728",
            "organisation":"Werbeagentur Gl\u00fcck","last_name":"zu Fall","first_name":"Rainer",
            "gender":"male",
            "notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,
            "tag_list":"!example","created_at":"2011-12-21T22:55:00+01:00","updated_at":"2012-02-02T20:07:36+01:00",
            "language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,
            "bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,
            "lock_version":1,"cash_discount":null,"due_days":null,
            "address_field":"Werbeagentur Gl\u00fcck\nHerr Rainer zu Fall\nKleeweg 4\n30001 Berlin",
            "addresses":[{"address":
                         {"id":"bUvub0lb4r4BelabxfpGMl","city":"Berlin","address1":"Kleeweg 4","address2":null,"pobox":"","zip":"30001",
                           "state":null,"country":null,"created_at":"2011-12-21T22:55:00+01:00","updated_at":"2011-12-21T22:55:00+01:00",
                           "address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}
            }],
            "team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":null,
            "sales_potential":null,"probability":null,"expected_revenue":null}},
            "client_id":"bUvvUglb4r4BelabxfpGMl",
            "contact":
            {"contact":
            {"id":"bUvvUglb4r4BelabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-01012-728","organisation":"Werbeagentur Gl\u00fcck","last_name":"zu Fall","first_name":"Rainer","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"!example","created_at":"2011-12-21T22:55:00+01:00","updated_at":"2012-02-02T20:07:36+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":1,"cash_discount":null,"due_days":null,"address_field":"Werbeagentur Gl\u00fcck\nHerr Rainer zu Fall\nKleeweg 4\n30001 Berlin","addresses":
            [{"address":
            {"id":"bUvub0lb4r4BelabxfpGMl","city":"Berlin","address1":"Kleeweg 4","address2":null,"pobox":"","zip":"30001","state":null,"country":null,"created_at":"2011-12-21T22:55:00+01:00","updated_at":"2011-12-21T22:55:00+01:00","address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}}],
             "team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":null,"sales_potential":null,"probability":null,"expected_revenue":null},
             "links":[{"rel":"self","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"instances","href":"contacts"},
                      {"rel":"destroy","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"update","href":"contacts/bUvvUglb4r4BelabxfpGMl"},
                      {"rel":"create","href":"contacts"},
                      {"rel":"documents","href":"contacts/bUvvUglb4r4BelabxfpGMl/documents"},
                      {"rel":"attachments","href":"contacts/bUvvUglb4r4BelabxfpGMl/attachments"},
                      {"rel":"invoices","href":"contacts/bUvvUglb4r4BelabxfpGMl/invoices"},
                      {"rel":"estimates","href":"contacts/bUvvUglb4r4BelabxfpGMl/estimates"},
                      {"rel":"orders","href":"contacts/bUvvUglb4r4BelabxfpGMl/orders"},
                      {"rel":"credit_notes","href":"contacts/bUvvUglb4r4BelabxfpGMl/credit_notes"},
                      {"rel":"recurrings","href":"contacts/bUvvUglb4r4BelabxfpGMl/recurrings"},
                      {"rel":"payment_reminders","href":"contacts/bUvvUglb4r4BelabxfpGMl/payment_reminders"},
                      {"rel":"comments","href":"contacts/bUvvUglb4r4BelabxfpGMl/comments"},
                      {"rel":"emails","href":"contacts/bUvvUglb4r4BelabxfpGMl/emails"},
                      {"rel":"emails create","href":"contacts/bUvvUglb4r4BelabxfpGMl/emails"}]},
            "contact_id":"bUvvUglb4r4BelabxfpGMl","team_id":null,
            "line_items":[],
            "items":[],
           "created_at":"2011-12-21T22:55:01+01:00","updated_at":"2013-01-23T09:56:46+01:00","lock_version":1,"price_total":1950.0,"price_tax":0.0,"gross_total":1950.0,"tax_total":0.0,"net_total":1950.0,"net_total_base":1950.0,"cost_total":0.0,"gross_margin_total":1950.0,"gross_margin_pct":100.0,"recurring_id":null},
           "links":[{"rel":"self","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"instances","href":"invoices"},
                    {"rel":"destroy","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"update","href":"invoices/bUAr_Qlb4r4BelabxfpGMl"},
                    {"rel":"create","href":"invoices"},
                    {"rel":"attachments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/attachments"},
                    {"rel":"payments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payments"},
                    {"rel":"payment_reminders","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payment_reminders"},
                    {"rel":"comments","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/comments"},
                    {"rel":"emails","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/emails"},
                    {"rel":"emails create","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/emails"},
                    {"rel":"payment create","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/payments"},
                    {"rel":"print","href":"invoices/bUAr_Qlb4r4BelabxfpGMl/print"}]
}
'''.replace(u"\n", u"").replace(u"\t", u"").replace(u" ", u"")


class InvoiceWithDocumentAttachmentTestCase(SalesKingBaseTestCase):
    def test_invoice_noLineitem_instaciated_mock_success(self):
        clnt = api.APIClient()
        klass = resources.get_model_class("invoice", api=clnt)
        invoice = klass()
        response = MockInvoiceNoLineItemResponse()
        obj = invoice.to_instance(response)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.number, "R-069-2011-215")

    def test_invoice_instaciated_mock_fails(self):
        clnt = api.APIClient()
        klass = resources.get_model_class("invoice", api=clnt)
        invoice = klass()
        response = MockInvoiceResponse()
        obj = invoice.to_instance(response)
        self.assertEqual(obj.number, "R-069-2011-215a")
        self.assertEqual(obj['client']['client']['number'], "K-01012-728")
