# shopping-cart

create .travis.yml file in root directory with these contents:

    dist: xenial
    language: python
    python:
    - "3.7"
    install:
    - pip install pytest
    script:
    - pytest

## CI Status Badge
[![Build Status](https://travis-ci.com/wae10/shopping-cart.svg?branch=cleanup)](https://travis-ci.com/wae10/shopping-cart)

pip install pytest

create test folder, my_test.py

create conftest.py file for pytest

run: pytest

optional:

    pip install coverage

    coverage run shopping_cart.py

    coverage report

