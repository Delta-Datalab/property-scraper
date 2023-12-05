import pytest

from src.property import ZonaPropProperty
from src.propertyParser import PropertyParser


def test_validatePropertScrapperGivesCorrectPropertyType():
    domain = "www.zonaprop.com.ar"
    parser = PropertyParser()
    property_type = parser.get_propertyType(domain)

    assert isinstance(property_type, ZonaPropProperty)
