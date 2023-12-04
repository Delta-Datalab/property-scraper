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
        property_attributes = self._get_property_attributes(data)
        covered_area = f"{np.nan}"

        if property_attributes:
            count = 0
            first_appearance = f"{np.nan}"
            second_appearance = f"{np.nan}"
            for span in property_attributes:
                inner_span = span.find_all("span")
                for span_element in inner_span:
                    if "m²" in span_element.get_text():
                        print(span_element.get_text())
                        count = count + 1
                        if count == 1:
                            first_appearance = str(span_element.get_text().strip())
                            numeric_area1 = float(first_appearance.strip(" m²"))
                        if count == 2:
                            second_appearance = str(span_element.get_text().strip())
                            numeric_area2 = float(second_appearance.strip(" m²"))
            if count >= 2:
                if numeric_area1 >= numeric_area2:
                    covered_area = second_appearance
                else:
                    covered_area = first_appearance

        return covered_area

    def _get_property_attributes(self, data):
        property_attributes = data.find("div", {"data-qa": "POSTING_CARD_FEATURES"})
        property_attributes = property_attributes.find_all("span")
        return property_attributes

    def _find_property_attribute(self, data, attribute_name):
        property_attribute = f"{np.nan}"
        cont  = 0
        for span in data:
            span_inner_elements = span.find_all("span")
            for inner_span in span_inner_elements:
                if attribute_name in inner_span.get_text():
                    property_attribute = str(inner_span.get_text().strip())
                    
        return property_attribute
