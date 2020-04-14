# shopping-cart/my_test.py

from shopping_cart import enlarge, to_usd

def test_enlarge():
    result = enlarge(3)
    assert result == 300

def test_to_usd():
    result = to_usd(3.50)
    assert result == "$3.50"