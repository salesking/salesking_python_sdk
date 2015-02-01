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

## Create a Contact
    
    from salesking import resources
    model = resources.get_model_class("contact")
    data = {"organisation": "first customer via py api", "type": "Client"}
    contact = model(data)
    contact = contact.save()
    
## Create contact with nested Address
    
    from salesking import resources
    model = resources.get_model_class("contact")
    contact = model()
    contact.organisation = "second customer"
    contact.type = "Lead"
    model = resources.get_model_class("address")
    address = model()
    address.city = u"Duisburg"
    address.address1 = u"Foo Street"
    address.address2 = u"Appartment Bar"
    address.address_type = u"work"
    contact.addresses = [address]
    contact = contact.save()
    print contact.get_data()

## List all contacts type Lead with salesking in the name
    # collection properties you could find here
    http://sk-api-browser.herokuapp.com/#contact click url params on the right
    
    # Paging details: 
    # GET second page with 100 in list, only id+name
    /contacts?per_page=100&page=2&fields=id,name    
    
    
    Example:
    
    from salesking import collection
    valid_filters = {u"organisation": u"salesking", u"type": u"Lead"}
    col = collection.get_collection_instance("contact")
    col.set_filters(valid_filters)
    col.load()
    items = col.get_items()
    for x in items:
     	print u"id: %s name: %s" % (x.id, x.organisation)
    col.reset_items()
    col.load(page=2)
    items = col.get_items()
    for x in col.items:
     	print u"id: %s name: %s" % (x.id, x.organisation)



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


## Running the tests ## 
#######################

1) create a fresh virtualenv

2) activate the virtualenv

3) run pip install -e .\salesking

4) configure your local_settings.py

5) run python -m unittest tests (logger silenced)


#Sidenotes:
###########

This SDK uses the automatic jsonschema validation of properties,
in order to make it work, it removes porperties from the recieved
data, that are containing None values, this means you have
to wrap any data access in a try: except block...
