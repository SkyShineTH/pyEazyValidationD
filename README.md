# pyEazyValidationD
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus blandit est sem, quis interdum ex sodales vitae. Mauris sit amet pretium elit. Vestibulum vel nulla tellus. Nulla eu consectetur ligula. In condimentum ut velit vel malesuada. Nulla odio massa, tincidunt vel convallis quis, dictum sagittis sapien. Vivamus quis ex suscipit, bibendum magna id, fringilla metus. Nulla nec pellentesque lectus. Donec vitae sem tellus. Nunc a turpis condimentum neque interdum vulputate. Proin facilisis enim neque, ut lobortis eros venenatis eu.

Donec vulputate faucibus lectus, id vehicula lectus accumsan id. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur diam mauris, pharetra vel neque ut, molestie dictum magna. Aliquam ornare odio id ex pharetra, eu tincidunt metus malesuada. Nullam erat libero, consequat id viverra ut, lobortis id justo. Mauris pellentesque lacus eu felis auctor, vel placerat lectus cursus. Nulla ultricies porta malesuada.

Duis quis condimentum tellus, a vulputate ex. Nam nec nulla vel orci viverra imperdiet quis sed lacus. Nulla feugiat euismod mollis. Donec dapibus bibendum orci, in congue magna porta ac. Vivamus lacinia dui at ante pharetra tristique. Nulla sit amet pretium nunc. Aliquam a odio at odio euismod ullamcorper. Vivamus nunc risus, ultrices ultricies arcu eu, feugiat semper arcu. Cras sagittis orci sit amet enim bibendum, eu vulputate ex vulputate. Etiam placerat egestas sapien non pretium. Vestibulum venenatis ligula sed turpis vehicula, imperdiet pulvinar erat luctus. Nulla tempus sem ac ornare tincidunt. Nunc tincidunt enim tempor dolor fringilla, sit amet viverra libero luctus.

## Run Locally

Clone the project

```bash
  git clone https://github.com/SkyShineTH/pyEazyValidationD.git
```

Go to the project pyEazyValidationD

```bash
  cd my-project
```
## Usage/Examples

```python
from datavalidator import validate_type, validate_length, validate_regex, validate_range, ValidationError

try:
    validate_type(123, int)
    validate_length("hello", min_length=3)
    validate_regex("example@mail.com", r'^\S+@\S+\.\S+$')
    validate_range(10, min_value=5, max_value=15)
except ValidationError as e:
    print(f'Validation error: {e}')
```


## Running Tests

To run tests, run the following command

```bash
  python .\tests\test_validators.py
```



## Authors

- [@SkyShineTH](https://github.com/SkyShineTH)

