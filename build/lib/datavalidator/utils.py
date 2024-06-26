import re

def is_integer(value):
    return isinstance(value, int)

def is_float(value):
    return isinstance(value, float)

def is_string(value):
    return isinstance(value, str)

def matches_regex(value, pattern):
    return re.match(pattern, value) is not None
