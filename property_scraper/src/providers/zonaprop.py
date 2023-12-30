from src.providers.provider import Provider

import pandas as pd
import logging


class zonapropProvider(Provider):
    def __init__(self, providerHTMLData, aProviderURL):
        super().__init__(providerHTMLData)
        self.url = aProviderURL

    def getDataFromProperties(self):
        propertiesData = {
            "url": self.getPropertiesURLs(),
            "price": self.getPropertiesPrices(),
            "currency": self.getPropertiesCurrencies(),
            "expenses": self.getPropertiesExpenses(),
            "expenses_currency": self.getPropertiesExpensesCurrencies(),
            "location": self.getPropertiesLocations(),
            "total_area": self.getPropertiesTotalAreas(),
            "covered_area": self.getPropertiesCoveredAreas(),
            "total_rooms": self.getPropertiesTotalRooms(),
            "bedrooms": self.getPropertiesBedrooms(),
            "bathrooms": self.getPropertiesBathrooms(),
            "reserved": self.getPropertiesReserved(),
            "parking": self.getPropertiesParkings(),
            "real_state_agency": self.getPropertiesRealStateAgencies(),
            "description": self.getPropertiesDescriptions(),
        }

        return pd.DataFrame(propertiesData)

    def getNextPageURL(self):
        if "pagina-" in self.url:
            page = int(self.url.split("-")[-1].split(".")[0]) + 1
            return self.url.replace(f"-pagina-{page-1}.html", f"-pagina-{page}.html")
        else:
            return self.url.replace(".html", f"-pagina-{2}.html")

    def _propertyAttributesLogger(self, func, res):
        if pd.isna(res):
            logging.warning(
                f"Property attribute data from {self.url} is NaN using {func.__name__}."
            )
        else:
            logging.info(
                f"Property attribute data from {self.url} is found using {func.__name__}."
            )

    def _getPropertyData(func):
        def getPropertyAttributes(self):
            propertiesDataDivs = self.data.find_all(
                "div", {"data-posting-type": "PROPERTY"}
            )
            attributeData = []

            for propertyDataDiv in propertiesDataDivs:
                try:
                    res = func(self, propertyDataDiv)
                    self._propertyAttributesLogger(func, res)
                except Exception as e:
                    logging.error(
                        f"Error while scraping property attribute data from {self.url} using {func.__name__}."
                    )
                    logging.error(e)
                    res = pd.NA
                attributeData.append(res)

            return pd.Series(attributeData)

        return getPropertyAttributes

    @_getPropertyData
    def getPropertiesPrices(self, propertyDataDiv):
        priceDiv = propertyDataDiv.find("div", {"data-qa": "POSTING_CARD_PRICE"})
        if priceDiv is None:
            return pd.NA
        return str(priceDiv.text)

    @_getPropertyData
    def getPropertiesExpenses(self, propertyDataDiv):
        expenses_element = propertyDataDiv.find("div", {"data-qa": "expensas"})

        if expenses_element is None:
            return pd.NA
        else:
            expenses = str(expenses_element.text.strip())

        return expenses

    @_getPropertyData
    def getPropertiesExpensesCurrencies(self, propertyDataDiv):
        currency = pd.NA
        expenses_element = propertyDataDiv.find("div", {"data-qa": "expensas"})
        if expenses_element is None:
            expense = pd.NA
        else:
            expense = str(expenses_element.text.strip())

        if pd.isna(expense):
            return currency
        elif expense[0] == "U":
            currency = "USD"
        elif expense[0] == "$":
            currency = "$"

        return currency

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
        priceDiv = propertyDataDiv.find("div", {"data-qa": "POSTING_CARD_PRICE"})
        if priceDiv is None:
            return pd.NA
        price = str(priceDiv.text)

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
