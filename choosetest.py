import pytest
from datetime import datetime
from choose import choose



def test_is_before_true():
    date1 = datetime.strptime('2015-05-07', '%Y-%m-%d')
    date2 = datetime.strptime('2015-06-07', '%Y-%m-%d')
    assert is_before(date1, date2) is True

def test_is_before_false():
    date1 = datetime.strptime('2015-06-07', '%Y-%m-%d')
    date2 = datetime.strptime('2015-05-07', '%Y-%m-%d')
    assert is_before(date1, date2) is False
def test_is_same_true():
    date1 = datetime.strptime('2015-05-07', '%Y-%m-%d')
    date2 = datetime.strptime('2015-05-07', '%Y-%m-%d')
    assert is_same(date1, date2) is True

def test_is_same_false():
    date1 = datetime.strptime('2015-05-07', '%Y-%m-%d')
    date2 = datetime.strptime('2016-05-07', '%Y-%m-%d')
    assert is_same(date1, date2) is False
