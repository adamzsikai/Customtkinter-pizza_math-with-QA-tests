import pytest

from unit_pm import main

def test_basic_calculation1():
    assert main(100,2,500,200,3,1000) == ("15707.95","1000.00","0.0637","94247.78","3000","0.03182")

def test_basic_calculation2():
    assert main(20,1,1400,16,2,900) == ("314.16","1400","4.56","402.12","1800","4.48")

def test_basic_calculation3():
    assert main(50,1,7000,32,2,3500) == ("1962.50","7000.00","3.5669","1607.68","7000.00","4.3541")

def test_basic_calculation4():
    assert main(32,2,3500,50,1,7000) == ("1607.68","7000.00","4.3541","1962.50","7000.00","3.5669")

def test_basic_calculation5():
    assert main(32,2,3700,50,1,7300) == ("1607.68","7400.00","4.6029","1962.50","7300.00","3.7197")



def test_string_input():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")

def test_float_input():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")

def test_stringfloat_input():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")


    

def test_edge_cases():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")

def test_zero_inputs():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")

def test_neggative_inputs():
    assert main("a1","b1","c1","a2","b2","c2") == ("Error!","Error!","Error!","Error!","Error!","Error!")


