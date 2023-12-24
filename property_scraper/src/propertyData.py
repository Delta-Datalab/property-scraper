import numpy as np
import pandas as pd


class PropertyData:
    def __init__(
        self,
        price,
        expenses,
        expenses_type,
        bathrooms,
        bedrooms,
        total_rooms,
        covered_area,
        total_area,
        currency,
        description,
        parking,
        url,
        location,
        real_state_agency,
        reserved,
    ):
        self.price = price
        self.expenses = expenses
        self.expenses_type = expenses_type
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.total_rooms = total_rooms
        self.covered_area = covered_area
        self.total_area = total_area
        self.currency = currency
        self.description = description
        self.parking = parking
        self.url = url
        self.location = location
        self.real_state_agency = real_state_agency
        self.reserved = reserved

    def addTo(self, dataframe):
        dataframe.loc[len(dataframe.index)] = [
            self.url,
            self.price,
            self.currency,
            self.expenses,
            self.expenses_type,
            self.location,
            self.total_area,
            self.covered_area,
            self.total_rooms,
            self.bathrooms,
            self.bedrooms,
            self.parking,
            self.real_state_agency,
            self.reserved,
            self.description,
        ]
