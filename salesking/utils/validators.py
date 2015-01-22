#!/usr/bin/env python
# -*- coding: utf-8 -*-

import iso8601
import validictory

from validictory.validator import DEFAULT_FORMAT_VALIDATORS


def validate_format_iso8601(validator, fieldname, value, format_option):
    """
    validates the iso8601 format
    raises value error if the value for fieldname does not match the format
    is iso8601 eg #"2007-06-20T12:34:40+03:00"
    """
    try:
        iso8601.parse_date(value)
    except ValueError:
        raise ValidationError(
            "Value %(value)r of field '%(fieldname)s' is not in "
            "'iso8601 YYYY-MM-DDThh:mm:ss(+/-)hh:mm' format" % locals())

def validate_format_text(validator, fieldname, value, format_option):
    """
    validates format text- always valid
    """
    pass

def json_schema_validation_format(value, schema_validation_type):
    """
    adds iso8601 to the datetimevalidator
    raises SchemaError if validation fails
    """
    DEFAULT_FORMAT_VALIDATORS['date-time'] = validate_format_iso8601
    DEFAULT_FORMAT_VALIDATORS['text'] = validate_format_text
    validictory.validate(value, schema_validation_type, format_validators=DEFAULT_FORMAT_VALIDATORS)
    

