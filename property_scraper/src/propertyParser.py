import numpy as np

from src.property import ZonaPropProperty

class PropertyParser: 
    def __init__(self):
        pass
        
    def get_propertyType(self, domain):
        if domain == "www.zonaprop.com.ar":
            property_type = ZonaPropProperty()
        else:
            raise ValueError("Invalid type of Property")

        return (property_type)