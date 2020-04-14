# shopping-cart/my_test.py

from shopping_cart import enlarge, to_usd, human_friendly_timestamp

def test_enlarge():
    result = enlarge(3)
    assert result == 300

def test_to_usd():
    result = to_usd(3.50)
    assert result == "$3.50"

def test_human_friendly_timestamp():
    date = "2020-04-13 11:17:49.644685"
    result = human_friendly_timestamp(date)
    assert result == "2020-04-13 11:17 AM"

