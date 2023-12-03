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
    
    def get_covered_area(self,data):
        covered_area_element = data.find("div", {"data-qa": "POSTING_CARD_FEATURES"})
        covered_area = f"{np.nan}"

        if covered_area_element:
            span_elements = covered_area_element.find_all("span")
            for span in span_elements:
                image = span.find("img", {"src": "https://img10.naventcdn.com/listado/RPLISv8.62.0-RC3/images/featuresSprite.png", "class": "sc-1uhtbxc-1 dRoEma"})
                if image:
                    span_inner_element = image.find_next_sibling("span")
                    covered_area = str(span_inner_element.get_text().strip())

        return covered_area
