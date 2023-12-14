import numpy as np
import pandas as pd


class Property:
    def __init__(self, property_data, property_type):
        self.data = property_data
        self.property_type = property_type

    def get_price(self):
        """Get the price of the property.

        Returns:
            The price of the property.
        """

        return (self.property_type).get_price(self.data)

    def get_expenses(self):
        """Get the expenses for the property.

        Returns:
            The expenses for the property.
        """

        return (self.property_type).get_expenses(self.data)

    def get_expenses_type(self):
        """Get the type of expenses for the property.

        Returns:
            The type of expenses for the property.
        """

        return (self.property_type).get_expenses_type(self.data)

    def get_bathrooms(self):
        """Get the number of bathrooms for the property.

        Returns:
            The number of bathrooms for the property.
        """

        return (self.property_type).get_bathrooms(self.data)

    def get_bedrooms(self):
        """Get the number of bedrooms for the property.

        Returns:
            The number of bedrooms for the property.
        """

        return (self.property_type).get_bedrooms(self.data)

    def get_total_rooms(self):
        """Get the number of total rooms for the property.

        Returns:
            The number of total rooms for the property.
        """

        return (self.property_type).get_total_rooms(self.data)

    def get_covered_area(self):
        """Get the covered area for the property.

        Returns:
            The covered area for the property.
        """

        return (self.property_type).get_covered_area(self.data)

    def get_total_area(self):
        """Get the total area for the property.

        Returns:
            The total area for the property.
        """

        return (self.property_type).get_total_area(self.data)

    def get_currency(self):
        """Get the price of the property.

        Returns:
            The price of the property.
        """

        return (self.property_type).get_currency(self.data)

    def get_description(self):
        """Get the description for the property.

        Returns:
            The description for the property.
        """

        return (self.property_type).get_description(self.data)

    def get_parking(self):
        """Get the parking for the property.

        Returns:
            The parking for the property.
        """

        return (self.property_type).get_parking(self.data)

    def get_url(self):
        """Get the url for the property.

        Returns:
            The url for the property.
        """

        return (self.property_type).get_url(self.data)

    def get_location(self):
        """Get the location for the property.

        Returns:
            The location for the property.
        """

        return (self.property_type).get_location(self.data)


class ZonaPropProperty:
    def get_price(self, data):
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)
        return price

    def get_expenses(self, data):
        expenses_element = data.find("div", {"data-qa": "expensas"})

        if expenses_element:
            expenses = str(
                expenses_element.text.strip()
            )  # Extract text and remove leading/trailing spaces
        else:
            expenses = pd.NA  # Assign NaN if expenses_element is not found

        return expenses

    def get_expenses_type(self, data):
        expensesType = pd.NA
        expenses = self.get_expenses(data)

        if pd.isna(expenses):
            return expensesType
        if expenses[0] == "U":
            expensesType = "USD"
        if expenses[0] == "$":
            expensesType = "$"

        return expensesType

    def get_bathrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bathrooms = self._find_property_attributes(property_attributes, "baño")

        return bathrooms

    def get_bedrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bedrooms = self._find_property_attributes(property_attributes, "dorm.")

        return bedrooms

    def get_total_rooms(self, data):
        property_attributes = self._get_property_attributes(data)
        total_rooms = self._find_property_attributes(property_attributes, "amb.")

        return total_rooms

    def get_covered_area(self, data):
        property_attributes = self._get_property_attributes(data)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        covered_area = self._select_area_for_covered_area(property_area_attributes)

        return covered_area

    def get_total_area(self, data):
        property_attributes = self._get_property_attributes(data)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        total_area = self._select_area_for_total_area(property_area_attributes)

        return total_area

    def _findAreasFromPropertyAttributes(self, property_attributes):
        property_area_attributes = self._find_property_attributes(
            property_attributes, "m²", multipleAttributes=True
        )
        self._forEachAreaStripMeasureAndConvertToInteger(property_area_attributes)

        return property_area_attributes

    def _select_area_for_total_area(self, property_area_attributes):
        if len(property_area_attributes) == 0:
            total_area = pd.NA
        else:
            total_area = max(property_area_attributes)
        return total_area

    def _forEachAreaStripMeasureAndConvertToInteger(self, property_area_attribute):
        for i in range(len(property_area_attribute)):
            property_area_attribute[i] = int(property_area_attribute[i].strip(" m²"))

    def _select_area_for_covered_area(self, property_area_attributes):
        if len(property_area_attributes) <= 1:
            covered_area = pd.NA
        else:
            covered_area = min(property_area_attributes)
        return covered_area

    def get_currency(self, data):
        currency = pd.NA
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)

        if price:
            if price[0] == "U":
                currency = "USD"
            if price[0] == "$":
                currency = "$"

        return currency

    def get_description(self, data):
        description = pd.NA
        description_element = data.find("div", {"data-qa": "POSTING_CARD_DESCRIPTION"})

        if description_element:
            description = str(description_element.get_text().strip())

        return description

    def get_parking(self, data):
        property_attributes = self._get_property_attributes(data)
        parking = self._find_property_attributes(property_attributes, "coch.")

        return parking

    def get_url(self, data):
        url = pd.NA
        property_div_url = data.get("data-to-posting")
        if property_div_url:
            url = property_div_url

        return url

    def get_location(self, data):
        location = pd.NA
        location_element = data.find("div", {"data-qa": "POSTING_CARD_LOCATION"})

        if location_element:
            location = str(location_element.get_text().strip())

        return location

    def _get_property_attributes(self, data):
        property_attributes = data.find("div", {"data-qa": "POSTING_CARD_FEATURES"})
        property_attributes = property_attributes.find_all("span")
        return property_attributes

    def _find_property_attributes(self, data, attribute_name, multipleAttributes=False):
        property_attributes = []

        self._forSpanInDataFindAllTheAttributesWith(
            data, attribute_name, property_attributes
        )

        if property_attributes:
            if multipleAttributes:
                return property_attributes
            else:
                return property_attributes[0]

        return pd.NA

    def _forSpanInDataFindAllTheAttributesWith(
        self, data, attribute_name, property_attributes
    ):
        for span in data:
            span_inner_elements = span.find_all("span")
            for inner_span in span_inner_elements:
                if attribute_name in inner_span.get_text():
                    property_attributes.append(str(inner_span.get_text().strip()))
