# shopping-cart

## CI Status Badge
[![Build Status](https://travis-ci.com/wae10/shopping-cart.svg?branch=cleanup)](https://travis-ci.com/wae10/shopping-cart)

create .travis.yml file in root directory with these contents:

    dist: xenial
    language: python
    python:
    - "3.7"
    install:
    - pip install pytest
    script:
    - pytest

pip install pytest

## create test folder, my_test.py inside test folder

## create conftest.py file in root directory for pytest

to run: pytest

## optional:

    pip install coverage

    coverage run shopping_cart.py

    coverage report

