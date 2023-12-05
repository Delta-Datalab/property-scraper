import numpy as np


class Property:
    def __init__(self, property_data, domain):
        self.data = property_data

        if domain == "www.zonaprop.com.ar":
            self.property_type = ZonaPropProperty()
        else:
            raise ValueError("Invalid type of Property")

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

    def get_currency(self):
        """Get the price of the property.

        Returns:
            The price of the property.
        """

        return (self.property_type).get_currency(self.data)

    def get_currency(self):
        """Get the price of the property.

        Returns:
            The price of the property.
        """

        return (self.property_type).get_currency(self.data)

    def get_parking(self):
        """Get the parking for the property.

        Returns:
            The parking for the property.
        """

        return (self.property_type).get_parking(self.data)


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
            expenses = f"{np.nan}"  # Assign NaN if expenses_element is not found

        return expenses

    def get_bathrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bathrooms = self._find_property_attribute(property_attributes, "baño")

        return bathrooms

    def get_bedrooms(self, data):
        property_attributes = self._get_property_attributes(data)
        bedrooms = self._find_property_attribute(property_attributes, "dorm.")

        return bedrooms

    def get_total_rooms(self, data):
        property_attributes = self._get_property_attributes(data)
        total_rooms = self._find_property_attribute(property_attributes, "amb.")

        return total_rooms

    def get_covered_area(self, data):
        covered_area_element = data.find("div", {"data-qa": "POSTING_CARD_FEATURES"})
        covered_area = f"{np.nan}"

        if covered_area_element:
            span_elements = covered_area_element.find_all("span")
            for span in span_elements:
                image = span.find(
                    "img",
                    {
                        "src": "https://img10.naventcdn.com/listado/RPLISv8.62.0-RC3/images/featuresSprite.png",
                        "class": "sc-1uhtbxc-1 dRoEma",
                    },
                )
                if image:
                    span_inner_element = image.find_next_sibling("span")
                    covered_area = str(span_inner_element.get_text().strip())

        return covered_area

    def get_currency(self, data):
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)

        if price:
            if price == "Consultar precio":
                currency = str(np.nan)
            else:
                if price[0] == "U":
                    currency = "USD"
                else:
                    currency = "$"

        return currency

    def get_currency(self, data):
        currency = str(np.nan)
        price = str(data.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)

        if price[0] == "U":
            currency = "USD"
        if price[0] == "$":
            currency = "$"

        return currency

    def get_parking(self, data):
        property_attributes = self._get_property_attributes(data)
        parking = self._find_property_attribute(property_attributes, "coch.")

        return parking

    def _get_property_attributes(self, data):
        property_attributes = data.find("div", {"data-qa": "POSTING_CARD_FEATURES"})
        property_attributes = property_attributes.find_all("span")
        return property_attributes

    def _find_property_attribute(self, data, attribute_name):
        property_attribute = f"{np.nan}"
        for span in data:
            span_inner_elements = span.find_all("span")
            for inner_span in span_inner_elements:
                if attribute_name in span.get_text():
                    property_attribute = str(span.get_text().strip())

        return property_attribute
