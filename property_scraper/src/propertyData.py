import numpy as np
import pandas as pd


class PropertyData:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def addTo(self, propertiesDataframe):
        """
        Add property data to the given properties dataframe.

        Args:
            propertiesDataframe (pandas.DataFrame): The dataframe to which the property data will be added.

        Returns:
            None
        """
        rowPropertyData = {
            "url": self.url,
            "price": self.price,
            "currency": self.currency,
            "expenses": self.expenses,
            "expenses_currency": self.expenses_currency,
            "location": self.location,
            "total_area": self.total_area,
            "covered_area": self.covered_area,
            "total_rooms": self.total_rooms,
            "bathrooms": self.bathrooms,
            "bedrooms": self.bedrooms,
            "parking": self.parking,
            "real_state_agency": self.real_state_agency,
            "reserved": self.reserved,
            "description": self.description,
        }

        propertiesDataframe.loc[len(propertiesDataframe)] = rowPropertyData
