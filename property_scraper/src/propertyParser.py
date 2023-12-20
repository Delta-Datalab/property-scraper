import numpy as np

from src.provieder import zonapropProvieder


class PropertyParser:
    def __init__(self):
        pass

    def get_propertyType(self, domain):
        if domain == "www.zonaprop.com.ar":
            property_type = zonapropProvieder()
        else:
            raise ValueError("Invalid type of Property")

        return property_type
