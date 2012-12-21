# SalesKing Python SDK (beta)

Online CRM / Invoicing integration and
Business Cockpit one REST call away.

You never need to build your Customer Invoicing
yourself again.

The SDK wraps the REST json schema API.

## install

	pip install salesking-pyhton-sdk


## How the SDK works

# Examples

## Create a Client
	
	>>> from salesking import api, resources
	>>> clnt = api.APIClient()
    >>> model = resources.get_model_class("client",api=clnt)
    >>> data = {"organisation": "first customer"}
    >>> client = model(data)
    >>> client = client.save()


## What you need to do in order to start

1) Take a look at the api
	
	* http://www.salesking.eu/dev/
	* http://www.salesking.eu/dev/docs/
	* http://www.salesking.eu/dev/api/
	
2) Browse the schema
	
	* http://sk-api-browser.heroku.com   
   
3) Request a DEVELOPMENT USER   


4) create a local_settings.py in conf/ 

5) edit your details in local_settings.py
 
 
