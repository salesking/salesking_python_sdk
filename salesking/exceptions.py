class SalesKingException(Exception):
    
    def __init__(self, code, message, errors = None,**kwargs):
        self.code = code
        self.msg = message
        self.errors = errors
        super(SalesKingException,self).__init__(**kwargs)

class APIException(SalesKingException):
    """
    API Exceptions 
    """
    def __repr__(self):
        return "<APIException> %s %s %s" % (self.code,self.msg,self.errors)


class HttpError(Exception):
    """HTTP error"""


class BadHttpStatus(HttpError):
    """Invalid HTTP status"""

    def __init__(self, response):
        message = '%s returned an invalid status code: %s' \
                  % (response.url, response.status_code)
        super(BadHttpStatus, self).__init__(message, response=response)
        
class ClientError(Exception): pass
class ServerError(Exception): pass
class BadRequest(SalesKingException): pass
class UnprocessableEntity(BadRequest): pass
class Unauthorized(SalesKingException): pass
class NotFound(ClientError): pass
class Unavailable(Exception): pass