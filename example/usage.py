from datavalidator import validate_type, validate_length, validate_regex, validate_range, ValidationError

try:
    validate_type(123, int)
    validate_length("hello", min_length=3)
    validate_regex("example@mail.com", r'^\S+@\S+\.\S+$')
    validate_range(10, min_value=5, max_value=15)
except ValidationError as e:
    print(f'Validation error: {e}')