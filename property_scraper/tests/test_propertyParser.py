import pytest

from src.provieder import zonapropProvieder
from src.propertyParser import PropertyParser


def test_validatePropertScrapperGivesCorrectPropertyType():
    domain = "www.zonaprop.com.ar"
    parser = PropertyParser()
    property_type = parser.get_propertyType(domain)

    assert isinstance(property_type, zonapropProvieder)
