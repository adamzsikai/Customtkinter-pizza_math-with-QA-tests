import pytest

from unit_test_pm import main


def test_basic():
    assert main(50,1,7000,32,2,3500) == ("1962.50","7000.00","3.5669","1607.68","7000.00","4.3541")

def test_string():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")
