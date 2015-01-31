"""
helper for schema dereferencing
"""


def _value_properties_are_referenced(val):
    """
    val is a dictionary
    :param val:
    :return: True/False
    """
    if ((u'properties' in val.keys()) and
            (u'$ref' in val['properties'].keys())):
        return True
    return False


def _value_is_required(val):
    """
    val is a dictionary
    :param val:
    :return: True/False
    """
    if ((u'required' in val.keys()) and
            (val['required'] is True)):
        return True
    return False


def _value_is_default_any(val):
    if ((u'default' in val.keys()) and
            (u'any' == val['default'])):
        return True
    return False


def _value_has_items_key(val):
    if (u'items' in val.keys()):
        return True
    return False


def _value_is_type_text(val):
    """
    val is a dictionary
    :param val:
    :return: True/False
    """
    if ((u'type' in val.keys()) and
            (val['type'].lower() == u"text")):
        return True
    return False