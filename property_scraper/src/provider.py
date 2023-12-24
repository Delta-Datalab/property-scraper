import numpy as np
import pandas as pd

from src.propertyData import PropertyData


class Provider:
    def __init__(self, provider_data):
        self.data = provider_data
        self.properties = []

    def getDataFromProperties(self):
        propertiesDataframe = pd.DataFrame(
            columns=[
                "url",
                "price",
                "currency",
                "expenses",
                "expenses_type",
                "location",
                "total_area",
                "covered_area",
                "total_rooms",
                "bathrooms",
                "bedrooms",
                "parking",
                "real_state_agency",
                "reserved",
                "description",
            ]
        )

        for propertyData in self.properties:
            propertyData.addTo(propertiesDataframe)

        return propertiesDataframe


class zonapropProvider(Provider):
    def __init__(self, data):
        super().__init__(data)
        self.properties = self._collectPropertiesData(self.data)

    def getDataFromProperties(self):
        return super().getDataFromProperties()

    def _collectPropertiesData(self, data):
        data_qa_divs = data.find_all("div", {"data-posting-type": "PROPERTY"})

        properties = []

        for data_container in data_qa_divs:
            attributes = {
                "price": self._get_price(data_container),
                "expenses": self._get_expenses(data_container),
                "expenses_type": self._get_expenses_type(data_container),
                "bathrooms": self._get_bathrooms(data_container),
                "bedrooms": self._get_bedrooms(data_container),
                "total_rooms": self._get_total_rooms(data_container),
                "covered_area": self._get_covered_area(data_container),
                "total_area": self._get_total_area(data_container),
                "currency": self._get_currency(data_container),
                "description": self._get_description(data_container),
                "parking": self._get_parking(data_container),
                "url": self._get_url(data_container),
                "location": self._get_location(data_container),
                "real_state_agency": self._get_real_state_agency(data_container),
                "reserved": self._get_reserved(data_container),
            }
            property = PropertyData(**attributes)
            properties.append(property)

        return properties

    def _get_price(self, data):
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)
        return price

    def _get_expenses(self, data):
        expenses_element = data.find("div", {"data-qa": "expensas"})

        if expenses_element:
            expenses = str(
                expenses_element.text.strip()
            )  # Extract text and remove leading/trailing spaces
        else:
            return pd.NA  # Assign NaN if expenses_element is not found

        return expenses

    def _get_expenses_type(self, data):
        expensesType = pd.NA
        expenses = self._get_expenses(data)

        if pd.isna(expenses):
            return expensesType
        if expenses[0] == "U":
            expensesType = "USD"
        if expenses[0] == "$":
            expensesType = "$"

        return expensesType

    def _get_bathrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bathrooms = self._find_property_attributes(property_attributes, "baño")

        return bathrooms

    def _get_bedrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bedrooms = self._find_property_attributes(property_attributes, "dorm.")

        return bedrooms

    def _get_total_rooms(self, data):
        property_attributes = self._get_property_attributes(data)
        total_rooms = self._find_property_attributes(property_attributes, "amb.")

        return total_rooms

    def _get_covered_area(self, data):
        property_attributes = self._get_property_attributes(data)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        covered_area = self._select_area_for_covered_area(property_area_attributes)

        return covered_area

    def _get_total_area(self, data):
        property_attributes = self._get_property_attributes(data)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        total_area = self._select_area_for_total_area(property_area_attributes)

        return total_area

    def _get_currency(self, data):
        currency = pd.NA
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)

        if price:
            if price[0] == "U":
                currency = "USD"
            if price[0] == "$":
                currency = "$"

        return currency

    def _get_description(self, data):
        description = pd.NA
        description_element = data.find("div", {"data-qa": "POSTING_CARD_DESCRIPTION"})

        if description_element:
            description = str(description_element.get_text().strip())

        return description

    def _get_parking(self, data):
        property_attributes = self._get_property_attributes(data)
        parking = self._find_property_attributes(property_attributes, "coch.")

        return parking

    def _get_url(self, data):
        url = pd.NA
        property_div_url = data.get("data-to-posting")
        if property_div_url:
            url = property_div_url

        return url

    def _get_location(self, data):
        location = pd.NA
        location_element = data.find("div", {"data-qa": "POSTING_CARD_LOCATION"})

        if location_element:
            location = str(location_element.get_text().strip())

        return location

    def _get_real_state_agency(self, data):
        real_state_agency = False
        real_state_agency_element = data.find(
            "img", {"data-qa": "POSTING_CARD_PUBLISHER"}
        )

        if real_state_agency_element:
            real_state_agency = True

        return real_state_agency

    def _get_reserved(self, data):
        reserved = False
        reserved_element = data.find("span", {"color": "white"})

        if reserved_element and reserved_element.get_text() == "Reservado":
            reserved = True

        return reserved

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
