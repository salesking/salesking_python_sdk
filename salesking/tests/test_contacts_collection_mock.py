from salesking.tests.base import SalesKingBaseTestCase


class MockCollectionContactResponse(object):
    def __init__(self):
        self.status_code = 200
        self.content = u'''
{"contacts":
  [{"contact":{"id":"a55-akQyir5ld2abxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1286","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-01-31T20:49:11+01:00","updated_at":"2015-01-31T20:49:11+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg",
                "addresses":
                    [{"address":{"id":"a56cekQyir5ld2abxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-01-31T20:49:11+01:00","updated_at":"2015-01-31T20:49:11+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}
                    ],"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-01-31","sales_potential":null,"probability":null,"expected_revenue":null
         },
         "links":[{"rel":"self","href":"contacts/a55-akQyir5ld2abxfpGMl"},
                {"rel":"instances","href":"contacts"},
                {"rel":"destroy","href":"contacts/a55-akQyir5ld2abxfpGMl"},
                {"rel":"update","href":"contacts/a55-akQyir5ld2abxfpGMl"},
                {"rel":"create","href":"contacts"},
                {"rel":"documents","href":"contacts/a55-akQyir5ld2abxfpGMl/documents"},
                {"rel":"attachments","href":"contacts/a55-akQyir5ld2abxfpGMl/attachments"},
                {"rel":"invoices","href":"contacts/a55-akQyir5ld2abxfpGMl/invoices"},
                {"rel":"estimates","href":"contacts/a55-akQyir5ld2abxfpGMl/estimates"},
                {"rel":"orders","href":"contacts/a55-akQyir5ld2abxfpGMl/orders"},
                {"rel":"credit_notes","href":"contacts/a55-akQyir5ld2abxfpGMl/credit_notes"},
                {"rel":"recurrings","href":"contacts/a55-akQyir5ld2abxfpGMl/recurrings"},
                {"rel":"payment_reminders","href":"contacts/a55-akQyir5ld2abxfpGMl/payment_reminders"},
                {"rel":"comments","href":"contacts/a55-akQyir5ld2abxfpGMl/comments"},
                {"rel":"emails","href":"contacts/a55-akQyir5ld2abxfpGMl/emails"},
                {"rel":"emails create","href":"contacts/a55-akQyir5ld2abxfpGMl/emails"}]
},
{"contact":{"id":"a6N570lb8r4yBvabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-01012-911","organisation":"Funky Music Times","last_name":"Darwin","first_name":"George","gender":"male","notes":null,"position":null,"title":null,"tax_number":null,"vat_number":null,"email":"","url":null,"birthday":null,"tag_list":"!example","created_at":"2011-12-21T23:00:43+01:00","updated_at":"2012-02-02T20:06:01+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":1,"cash_discount":null,"due_days":null,"address_field":"Funky Music Times\nHerr George Darwin\n71 Brushfield St\nE1 6 Greater London",
  "addresses":
  [{"address":{"id":"a6N4dclb8r4yBvabxfpGMl","city":"Greater London","address1":"71 Brushfield St","address2":null,"pobox":"","zip":"E1 6","state":null,"country":null,"created_at":"2011-12-21T23:00:43+01:00","updated_at":"2011-12-21T23:00:43+01:00","address_type":null,"order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":null,"sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/a6N570lb8r4yBvabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/a6N570lb8r4yBvabxfpGMl"},
{"rel":"update","href":"contacts/a6N570lb8r4yBvabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/a6N570lb8r4yBvabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/a6N570lb8r4yBvabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/a6N570lb8r4yBvabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/a6N570lb8r4yBvabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/a6N570lb8r4yBvabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/a6N570lb8r4yBvabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/a6N570lb8r4yBvabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/a6N570lb8r4yBvabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/a6N570lb8r4yBvabxfpGMl/comments"},
{"rel":"emails","href":"contacts/a6N570lb8r4yBvabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/a6N570lb8r4yBvabxfpGMl/emails"}]},
{"contact":{"id":"aBJabEQFyr5lXDabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1292","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-02-01T10:38:41+01:00","updated_at":"2015-02-01T10:38:41+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aBJecGQFyr5lXDabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-02-01T10:38:41+01:00","updated_at":"2015-02-01T10:38:41+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-02-01","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aBJabEQFyr5lXDabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aBJabEQFyr5lXDabxfpGMl"},
{"rel":"update","href":"contacts/aBJabEQFyr5lXDabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aBJabEQFyr5lXDabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aBJabEQFyr5lXDabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aBJabEQFyr5lXDabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aBJabEQFyr5lXDabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aBJabEQFyr5lXDabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aBJabEQFyr5lXDabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aBJabEQFyr5lXDabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aBJabEQFyr5lXDabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aBJabEQFyr5lXDabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aBJabEQFyr5lXDabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aBJabEQFyr5lXDabxfpGMl/emails"}]},
{"contact":{"id":"aG92TWQJOr5kgsabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1324","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-02-01T18:45:36+01:00","updated_at":"2015-02-01T18:45:36+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aG96MmQJOr5kgsabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-02-01T18:45:36+01:00","updated_at":"2015-02-01T18:45:36+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-02-01","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aG92TWQJOr5kgsabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aG92TWQJOr5kgsabxfpGMl"},
{"rel":"update","href":"contacts/aG92TWQJOr5kgsabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aG92TWQJOr5kgsabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aG92TWQJOr5kgsabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aG92TWQJOr5kgsabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aG92TWQJOr5kgsabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aG92TWQJOr5kgsabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aG92TWQJOr5kgsabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aG92TWQJOr5kgsabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aG92TWQJOr5kgsabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aG92TWQJOr5kgsabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aG92TWQJOr5kgsabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aG92TWQJOr5kgsabxfpGMl/emails"}]},
{"contact":{"id":"aG_NccQxWr5i6tabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1284","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-01-31T20:05:32+01:00","updated_at":"2015-01-31T20:05:32+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aG_Rg-QxWr5i6tabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-01-31T20:05:32+01:00","updated_at":"2015-01-31T20:05:32+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-01-31","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aG_NccQxWr5i6tabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aG_NccQxWr5i6tabxfpGMl"},
{"rel":"update","href":"contacts/aG_NccQxWr5i6tabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aG_NccQxWr5i6tabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aG_NccQxWr5i6tabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aG_NccQxWr5i6tabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aG_NccQxWr5i6tabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aG_NccQxWr5i6tabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aG_NccQxWr5i6tabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aG_NccQxWr5i6tabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aG_NccQxWr5i6tabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aG_NccQxWr5i6tabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aG_NccQxWr5i6tabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aG_NccQxWr5i6tabxfpGMl/emails"}]},
{"contact":{"id":"aH8DLsP_Sr5kddabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1257","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-01-29T22:09:37+01:00","updated_at":"2015-01-29T22:09:37+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aH8I34P_Sr5kddabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-01-29T22:09:37+01:00","updated_at":"2015-01-29T22:09:37+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-01-29","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aH8DLsP_Sr5kddabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aH8DLsP_Sr5kddabxfpGMl"},
{"rel":"update","href":"contacts/aH8DLsP_Sr5kddabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aH8DLsP_Sr5kddabxfpGMl/emails"}]},
{"contact":{"id":"aIwYA6QIur5i6tabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1312","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-02-01T16:15:19+01:00","updated_at":"2015-02-01T16:15:19+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aIw2FIQIur5i6tabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-02-01T16:15:19+01:00","updated_at":"2015-02-01T16:15:19+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-02-01","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aIwYA6QIur5i6tabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aIwYA6QIur5i6tabxfpGMl"},
{"rel":"update","href":"contacts/aIwYA6QIur5i6tabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aIwYA6QIur5i6tabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aIwYA6QIur5i6tabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aIwYA6QIur5i6tabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aIwYA6QIur5i6tabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aIwYA6QIur5i6tabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aIwYA6QIur5i6tabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aIwYA6QIur5i6tabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aIwYA6QIur5i6tabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aIwYA6QIur5i6tabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aIwYA6QIur5i6tabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aIwYA6QIur5i6tabxfpGMl/emails"}]},
{"contact":{"id":"aK-e82QIir5khAabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1304","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-02-01T15:53:55+01:00","updated_at":"2015-02-01T15:53:55+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aK-i-cQIir5khAabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-02-01T15:53:55+01:00","updated_at":"2015-02-01T15:53:55+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-02-01","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aK-e82QIir5khAabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aK-e82QIir5khAabxfpGMl"},
{"rel":"update","href":"contacts/aK-e82QIir5khAabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aK-e82QIir5khAabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aK-e82QIir5khAabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aK-e82QIir5khAabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aK-e82QIir5khAabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aK-e82QIir5khAabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aK-e82QIir5khAabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aK-e82QIir5khAabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aK-e82QIir5khAabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aK-e82QIir5khAabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aK-e82QIir5khAabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aK-e82QIir5khAabxfpGMl/emails"}]},
{"contact":{"id":"aWCH9mQxSr5k6sabxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1279","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-01-31T19:58:48+01:00","updated_at":"2015-01-31T19:58:48+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"aWCL4WQxSr5k6sabxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-01-31T19:58:48+01:00","updated_at":"2015-01-31T19:58:48+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-01-31","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/aWCH9mQxSr5k6sabxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/aWCH9mQxSr5k6sabxfpGMl"},
{"rel":"update","href":"contacts/aWCH9mQxSr5k6sabxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/documents"},
{"rel":"attachments","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/estimates"},
{"rel":"orders","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/comments"},
{"rel":"emails","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/emails"},
{"rel":"emails create","href":"contacts/aWCH9mQxSr5k6sabxfpGMl/emails"}]},
{"contact":{"id":"adJ9O6QxGr5km4abxfpGMl","parent_id":null,"type":"Client","is_employee":false,"number":"K-2015-1271","organisation":"salesking","last_name":"Jane","first_name":"Dow","gender":null,"notes":"APITEST","position":null,"title":null,"tax_number":null,"vat_number":null,"email":"sales.py-api@mailinator.com","url":null,"birthday":null,"tag_list":"","created_at":"2015-01-31T19:36:04+01:00","updated_at":"2015-01-31T19:36:04+01:00","language":null,"currency":"EUR","payment_method":null,"bank_name":null,"bank_number":null,"bank_account_number":null,"bank_iban":null,"bank_swift":null,"bank_owner":null,"phone_fax":null,"phone_office":null,"phone_home":null,"phone_mobile":null,"lock_version":0,"cash_discount":null,"due_days":null,"address_field":"salesking\nDow Jane\nFoo Street\nAppartment Bar\nDuisburg","addresses":
  [{"address":{"id":"adKbTSQxGr5km4abxfpGMl","city":"Duisburg","address1":"Foo Street","address2":"Appartment Bar","pobox":null,"zip":null,"state":null,"country":null,"created_at":"2015-01-31T19:36:04+01:00","updated_at":"2015-01-31T19:36:04+01:00","address_type":"work","order":null,"lat":null,"long":null,"_destroy":false}}],
"team_id":null,"lead_source":null,"lead_ref":null,"lead_date":null,"converted_at":"2015-01-31","sales_potential":null,"probability":null,"expected_revenue":null},
"links":
  [{"rel":"self","href":"contacts/adJ9O6QxGr5km4abxfpGMl"},
{"rel":"instances","href":"contacts"},
{"rel":"destroy","href":"contacts/adJ9O6QxGr5km4abxfpGMl"},
{"rel":"update","href":"contacts/adJ9O6QxGr5km4abxfpGMl"},
{"rel":"create","href":"contacts"},
{"rel":"documents","href":"contacts/adJ9O6QxGr5km4abxfpGMl/documents"},
{"rel":"attachments","href":"contacts/adJ9O6QxGr5km4abxfpGMl/attachments"},
{"rel":"invoices","href":"contacts/adJ9O6QxGr5km4abxfpGMl/invoices"},
{"rel":"estimates","href":"contacts/adJ9O6QxGr5km4abxfpGMl/estimates"},
{"rel":"orders","href":"contacts/adJ9O6QxGr5km4abxfpGMl/orders"},
{"rel":"credit_notes","href":"contacts/adJ9O6QxGr5km4abxfpGMl/credit_notes"},
{"rel":"recurrings","href":"contacts/adJ9O6QxGr5km4abxfpGMl/recurrings"},
{"rel":"payment_reminders","href":"contacts/adJ9O6QxGr5km4abxfpGMl/payment_reminders"},
{"rel":"comments","href":"contacts/adJ9O6QxGr5km4abxfpGMl/comments"},
{"rel":"emails","href":"contacts/adJ9O6QxGr5km4abxfpGMl/emails"},
{"rel":"emails create","href":"contacts/adJ9O6QxGr5km4abxfpGMl/emails"}]}],"links":{"self":"https://frank.dev.salesking.eu/api/contacts?organisation=fb-&sort=ASC&per_page=10&page=1","next":"https://frank.dev.salesking.eu/api/contacts?organisation=fb-&sort=ASC&per_page=10&page=2"},"collection":{"current_page":1,"per_page":10,"total_entries":72,"total_pages":8}}
'''.replace(u"\n", u"").replace(u"\t", u"").replace(u" ", u"")


class ContactsCollectionMockTestCase(SalesKingBaseTestCase):
    pass