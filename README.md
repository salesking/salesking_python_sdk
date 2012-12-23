# SalesKing Python SDK (beta)

Your Business Cockpit one REST call away.
Online CRM / Invoicing integration / PDF Template

You never need to build your Customer Invoicing
yourself again.

The SDK wraps the REST json schema API.    

## Install
	
	>>> pip install salesking


## How the SDK works

# Examples

## Create a Client
	
	>>> from salesking import resources
	>>> model = resources.get_model_class("client")
    >>> data = {"organisation": "first customer"}
    >>> client = model(data)
    >>> client = client.save()
    
## Create Client with nested Address
	
	>>> from salesking import resources
	>>>	model = resources.get_model_class("client")
    >>> client = model()
    >>> client.organisation = "second customer"
    >>> model = resources.get_model_class("address")
    >>> address = model()
    >>> address.city = u"Duisburg"
    >>> address.address1 = u"Foo Street"
    >>> address.address2 = u"Appartment Bar"
    >>> address.address_type = u"work"
    >>> client.addresses = [address]
    >>> client = client.save()
    >>> print client.get_data()

## List all Clientss with salesking in the name
	
	>>> from salesking import collection
	>>> valid_filters = {u"q": u"salesking"}
    >>> col = collection.get_collection_instance("client")
    >>> col.set_filters(valid_filters)
    >>> col.load()
    >>> for x in col.items:
    >>> 	print "numbers %s" % x.number
        

## What you need to do in order to start

1) Register and activate a DEVELOPMENT USER at

	* https://dev.salesking.eu/signup   

2) Register Your app inside your salesking dev account


3) Take a look at the api
	
	* http://www.salesking.eu/dev/
	* http://www.salesking.eu/dev/docs/
	* http://www.salesking.eu/dev/api/
	
4) Browse the schema
	
	* http://sk-api-browser.heroku.com   

5) create a local_settings.py in site-packages/salesking/.conf  

6) edit your details in local_settings.py
 
7) have fun

# TODO:

	* Examples
	* Add Invoice
	* Send Invoice
