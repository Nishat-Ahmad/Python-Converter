import pytest
from project import temprature_caller
from project import angle_caller
from project import weight_caller
from project import currency_caller
from project import geometry_caller


def test_weight_caller():
    #Normal testing
    assert round(weight_caller("ounce", "pound", 10), 3) == 0.625
    assert round(weight_caller("pound", "gram", 10), 2) == 4535.92
    assert round(weight_caller("gram", "ounce", 10), 5) == 0.35274
    assert round(weight_caller("kilogram", "tonne", 10), 5) == 0.01
    assert weight_caller("tonne", "kilogram", 10) == 10000


def test_angle_caller():
    # Normal testing
    assert round(angle_caller("degree", "radian", 10), 6) == 0.174533
    assert round(angle_caller("degree", "gradian", 10), 4) == 11.1111
    assert round(angle_caller("radian", "degree", 10), 3) == 572.958
    assert round(angle_caller("radian", "gradian", 10), 2) == 636.62
    assert round(angle_caller("gradian", "radian", 10), 5) == 0.15708
    assert angle_caller("gradian", "degree", 10) == 9

def test_temprature_caller():
    # normal testing
    assert temprature_caller("celsius", "farenheit", 10) == 50
    assert temprature_caller("celsius", "kelvin", 10) == 283.15
    assert temprature_caller("kelvin", "farenheit", 1) == -457.87
    assert temprature_caller("kelvin", "celsius", 10) == -263.15
    assert round(temprature_caller("farenheit", "kelvin", 10), 3) == 260.928
    assert round(temprature_caller("farenheit", "celsius", 10), 4) == -12.2222

    # boundary test
    assert temprature_caller("celsius", "farenheit", 0) == 32
    assert temprature_caller("celsius", "kelvin", 0) == 273.15
    assert round(temprature_caller("kelvin", "farenheit", 0), 2) == -459.67

    # Extreme test
    assert temprature_caller("celsius", "farenheit", 10000) == 18032
    assert temprature_caller("celsius", "kelvin", 10000) == 10273.15
    assert round(temprature_caller("kelvin", "farenheit", 10000), 2) == 17540.33

    # abnormal test
    assert temprature_caller("xyz", "farenheit", 10000) == 0
    assert temprature_caller("celsius", "xyz", 10000) == 0
    with pytest.raises(TypeError):
        temprature_caller("kelvin", "farenheit", "xyz")


def test_geometry_caller():
    ...
    # This whole function was tested manually.

def test_currency_caller():
    ...
    # The test will fail due to ever changing value of fiat currency