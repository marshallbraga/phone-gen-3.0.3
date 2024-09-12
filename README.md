# phone-gen-3.0.3

# Phone Gen

[![PyPI](https://img.shields.io/pypi/v/phone-gen?color=%2301a001&label=pypi&logo=version)](https://pypi.org/project/phone-gen/)
[![Downloads](https://pepy.tech/badge/phone-gen)](https://pepy.tech/project/phone-gen)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/phone-gen.svg)](https://pypi.org/project/phone-gen/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/phone-gen)](https://github.com/tolstislon/phone-gen)  
[![Tests](https://github.com/tolstislon/phone-gen/workflows/tests/badge.svg)](https://github.com/tolstislon/phone-gen/actions/workflows/python-package.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

International phone number generation

**This module was created exclusively for generating test data**

## Installation

Install using pip:

```bash
pip install phone-gen
```

## Example

```python
from phone_gen import PhoneNumber

phone_number = PhoneNumber("US")  # ISO 3166-2
# or
phone_number = PhoneNumber("USA")  # ISO 3166-3
# or
phone_number = PhoneNumber("United state")  # Country name

# Get a phone number
number = phone_number.get_number()
print(number)  # +16067032572

# Get a country code
country_code = phone_number.get_code()
print(country_code)  # 1

# Get a phone number without a country code
number = phone_number.get_number(full=False)
print(number)  # 183782623

# Get a mobile phone number
number = phone_number.get_mobile()
print(number)  # +1423945549

# Get a national phone number
number = phone_number.get_national()
print(number)  # +17656234678
```

### pytest fixture

```python
import pytest
from phone_gen import PhoneNumber


@pytest.fixture
def phone_number():
    def wrap(code):
        return PhoneNumber(code).get_number()

    yield wrap


def test_one(phone_number):
    number = phone_number("GB")
    ...
```

## Using the CLI

```bash
usage: phone-gen [-h] [-v] [-n] country [country ...]

International phone number generation

positional arguments:
  country         Country code or country name. Example: "US" or "USA" or "United state"

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   show program's version number and exit
  -f, --not-full  Get a phone number without a country code
  -m, --mobile    Get mobile phone number
  -n, --national  Get national phone number
```

### Example

```bash
# Get a phone number
phone-gen GB
# +442408055065

phone-gen GBR
# +199968635

phone-gen Germany
# +447911899521

# Get a phone number without a country code
phone-gen -f DE
# 66999511

phone-gen -f Great britain
# 877595

# Get mobile phone number
phone-gen -m GB
# +442408055065

# Get national phone number
phone-gen -n DE
# +44540381
``

## Resources

- [Google's libphonenumber](https://github.com/google/libphonenumber)

## Changelog

- [Releases](https://github.com/tolstislon/phone-gen/releases)

## Contributing

**Contributions are very welcome.**

You might want to:

- Fix spelling errors
- Improve documentation
- Add tests for untested code
- Add new features
- Fix bugs

### Getting started

- Python 3.12
- Pipenv 2023.11.15+

1. Clone the repository:
    ```bash
   
    ```
2. Install dev dependencies:
    ```bash
    pipenv install --dev
    pipenv shell
    ```
3. Run black:
    ```bash
    pipenv run black
    ```
4. Run flake8:
    ```bash
    pipenv run flake8
    ```
5. Run the tests:
    ```bash
    pipenv run tests
    ```
