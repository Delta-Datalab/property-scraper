from src.providers.provider import Provider

import pandas as pd


class zonapropProvider(Provider):
    def __init__(self, providerHTMLData, aProviderURL):
        super().__init__(providerHTMLData)
        self.url = aProviderURL

    def getDataFromProperties(self):
        propertiesData = {
            "price": self.getPropertiesPrices(),
            "expenses": self.getPropertiesExpenses(),
            "expenses_currency": self.getPropertiesExpensesCurrencies(),
            "bathrooms": self.getPropertiesBathrooms(),
            "bedrooms": self.getPropertiesBedrooms(),
            "total_rooms": self.getPropertiesTotalRooms(),
            "covered_area": self.getPropertiesCoveredAreas(),
            "total_area": self.getPropertiesTotalAreas(),
            "currency": self.getPropertiesCurrencies(),
            "description": self.getPropertiesDescriptions(),
            "parking": self.getPropertiesParkings(),
            "url": self.getPropertiesURLs(),
            "location": self.getPropertiesLocations(),
            "real_state_agency": self.getPropertiesRealStateAgencies(),
            "reserved": self.getPropertiesReserved(),
        }

        return pd.DataFrame(propertiesData)

    def getNextPageURL(self):
        if "pagina-" in self.url:
            page = int(self.url.split("-")[-1].split(".")[0]) + 1
            return self.url.replace(f"-pagina-{page-1}.html", f"-pagina-{page}.html")
        else:
            return self.url.replace(".html", f"-pagina-{2}.html")

    def _getPropertyData(func):
        def getPropertyAttributes(self):
            propertiesDataDivs = self.data.find_all(
                "div", {"data-posting-type": "PROPERTY"}
            )
            attributeData = []

            for propertyDataDiv in propertiesDataDivs:
                attributeData.append(func(self, propertyDataDiv))

            return pd.Series(attributeData)

        return getPropertyAttributes

    @_getPropertyData
    def getPropertiesPrices(self, propertyDataDiv):
        price = str(propertyDataDiv.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)
        return price

    @_getPropertyData
    def getPropertiesExpenses(self, propertyDataDiv):
        expenses_element = propertyDataDiv.find("div", {"data-qa": "expensas"})

        if expenses_element:
            expenses = str(
                expenses_element.text.strip()
            )  # Extract text and remove leading/trailing spaces
        else:
            return pd.NA  # Assign NaN if expenses_element is not found

        return expenses

    def getPropertiesExpensesCurrencies(self):
        expenses = self.getPropertiesExpenses()

        expensesCurrency = []

        for expense in expenses:
            if pd.isna(expense):
                expensesCurrency.append(pd.NA)
            elif expense[0] == "U":
                expensesCurrency.append("USD")
            elif expense[0] == "$":
                expensesCurrency.append("$")
            else:
                expensesCurrency.append(pd.NA)

        return pd.Series(expensesCurrency)

    @_getPropertyData
    def getPropertiesBathrooms(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        bathrooms = self._find_property_attributes(property_attributes, "baño")

        return bathrooms

    @_getPropertyData
    def getPropertiesBedrooms(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        bedrooms = self._find_property_attributes(property_attributes, "dorm.")

        return bedrooms

    @_getPropertyData
    def getPropertiesTotalRooms(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        total_rooms = self._find_property_attributes(property_attributes, "amb.")

        return total_rooms

    @_getPropertyData
    def getPropertiesCoveredAreas(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        covered_area = self._select_area_for_covered_area(property_area_attributes)

        return covered_area

    @_getPropertyData
    def getPropertiesTotalAreas(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        property_area_attributes = self._findAreasFromPropertyAttributes(
            property_attributes
        )
        total_area = self._select_area_for_total_area(property_area_attributes)

        return total_area

    @_getPropertyData
    def getPropertiesCurrencies(self, propertyDataDiv):
        currency = pd.NA
        price = str(propertyDataDiv.find("div", {"data-qa": "POSTING_CARD_PRICE"}).text)

        if price:
            if price[0] == "U":
                currency = "USD"
            if price[0] == "$":
                currency = "$"

        return currency

    @_getPropertyData
    def getPropertiesDescriptions(self, propertyDataDiv):
        description = pd.NA
        description_element = propertyDataDiv.find(
            "div", {"data-qa": "POSTING_CARD_DESCRIPTION"}
        )

        if description_element:
            description = str(description_element.get_text().strip())

        return description

    @_getPropertyData
    def getPropertiesParkings(self, propertyDataDiv):
        property_attributes = self._get_property_attributes(propertyDataDiv)
        parking = self._find_property_attributes(property_attributes, "coch.")

        return parking

    @_getPropertyData
    def getPropertiesURLs(self, propertyDataDiv):
        url = pd.NA
        property_div_url = propertyDataDiv.get("data-to-posting")
        if property_div_url:
            url = property_div_url

        return url

    @_getPropertyData
    def getPropertiesLocations(self, propertyDataDiv):
        location = pd.NA
        location_element = propertyDataDiv.find(
            "div", {"data-qa": "POSTING_CARD_LOCATION"}
        )

        if location_element:
            location = str(location_element.get_text().strip())

        return location

    @_getPropertyData
    def getPropertiesRealStateAgencies(self, propertyDataDiv):
        real_state_agency = False
        real_state_agency_element = propertyDataDiv.find(
            "img", {"data-qa": "POSTING_CARD_PUBLISHER"}
        )

        if real_state_agency_element:
            real_state_agency = True

        return real_state_agency

    @_getPropertyData
    def getPropertiesReserved(self, propertyDataDiv):
        reserved = False
        reserved_element = propertyDataDiv.find("span", {"color": "white"})

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
