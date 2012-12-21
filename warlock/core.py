"""Core Warlock functionality"""

import copy
import model

from .errors import InvalidOperation
from .errors import ValidationError


"""Core Warlock functionality"""


def model_factory(schema, base_class=model.Model):
    """
    Generate a model class based on the provided JSON Schema
    :param schema: dict representing valid JSON schema
    :param base_class: BaseClass for the inheritance of the returning Model
    """
    schema = copy.deepcopy(schema)

    class Model(base_class):
        def __init__(self, *args, **kwargs):
            #super(base_class,self).__init__(schema,*args,**kwargs)
            base_class.__init__(self, schema,*args, **kwargs)
            
    Model.__name__ = str(schema['name'])
    #Model.__schema__ = schema
    return Model

