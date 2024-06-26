import re

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_type(value, expected_type):
    if not isinstance(value, expected_type):
        raise ValidationError(f'Expected type {expected_type.__name__}, got {type(value).__name__}')

def validate_length(value, min_length=None, max_length=None):
    if min_length is not None and len(value) < min_length:
        raise ValidationError(f'Length of value is less than {min_length}')
    if max_length is not None and len(value) > max_length:
        raise ValidationError(f'Length of value is greater than {max_length}')

def validate_regex(value, pattern):
    if not re.match(pattern, value):
        raise ValidationError('Value does not match the required pattern')

def validate_range(value, min_value=None, max_value=None):
    if min_value is not None and value < min_value:
        raise ValidationError(f'Value is less than {min_value}')
    if max_value is not None and value > max_value:
        raise ValidationError(f'Value is greater than {max_value}')