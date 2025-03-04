from src.providers.provider import Provider

import pandas as pd
import logging
import time


class zonapropProvider(Provider):
    def __init__(self, providerHTMLData, aProviderURL):
        super().__init__(providerHTMLData)
        self.url = aProviderURL

    def getDataFromProperties(self):
        return super().getDataFromProperties(self)

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
        expensesElement = propertyDataDiv.find("div", {"data-qa": "expensas"})

        if expensesElement is None:
            return pd.NA
        else:
            expenses = str(expensesElement.text.strip())

        return expenses

    @_getPropertyData
    def getPropertiesExpensesCurrencies(self, propertyDataDiv):
        currency = pd.NA
        expensesElement = propertyDataDiv.find("div", {"data-qa": "expensas"})
        if expensesElement is None:
            expense = pd.NA
        else:
            expense = str(expensesElement.text.strip())

        if pd.isna(expense):
            return currency
        elif expense[0] == "U":
            currency = "USD"
        elif expense[0] == "$":
            currency = "$"

        return currency

    @_getPropertyData
    def getPropertiesBathrooms(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        bathrooms = self._findPropertyAttributes(propertyAttributes, "baño")

        return bathrooms

    @_getPropertyData
    def getPropertiesBedrooms(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        bedrooms = self._findPropertyAttributes(propertyAttributes, "dorm.")

        return bedrooms

    @_getPropertyData
    def getPropertiesTotalRooms(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        totalRooms = self._findPropertyAttributes(propertyAttributes, "amb.")

        return totalRooms

    @_getPropertyData
    def getPropertiesCoveredAreas(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        coveredArea = self._findPropertyAttributes(propertyAttributes, "m² cub.")
        coveredArea = self._forAreaStripMeasureAndConvertToInteger(
            coveredArea, " m² cub."
        )

        return coveredArea

    @_getPropertyData
    def getPropertiesTotalAreas(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        totalArea = self._findPropertyAttributes(propertyAttributes, "m² tot.")
        totalArea = self._forAreaStripMeasureAndConvertToInteger(totalArea, " m² tot.")

        return totalArea

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
        descriptionElement = propertyDataDiv.find(
            "h3", {"data-qa": "POSTING_CARD_DESCRIPTION"}
        )

        if descriptionElement:
            description = str(descriptionElement.get_text().strip())

        return description

    @_getPropertyData
    def getPropertiesParkings(self, propertyDataDiv):
        propertyAttributes = self._getPropertyAttributes(propertyDataDiv)
        parking = self._findPropertyAttributes(propertyAttributes, "coch.")

        return parking

    @_getPropertyData
    def getPropertiesURLs(self, propertyDataDiv):
        url = pd.NA
        propertyDivUrl = propertyDataDiv.get("data-to-posting")
        if propertyDivUrl:
            url = propertyDivUrl

        return url

    @_getPropertyData
    def getPropertiesLocations(self, propertyDataDiv):
        location = pd.NA
        locationElement = propertyDataDiv.find(
            "h2", {"data-qa": "POSTING_CARD_LOCATION"}
        )

        if locationElement:
            location = str(locationElement.get_text().strip())

        return location

    @_getPropertyData
    def getPropertiesRealStateAgencies(self, propertyDataDiv):
        realStateAgency = False
        realStateAgencyElement = propertyDataDiv.find(
            "img", {"data-qa": "POSTING_CARD_PUBLISHER"}
        )

        if realStateAgencyElement:
            realStateAgency = True

        return realStateAgency

    @_getPropertyData
    def getPropertiesReserved(self, propertyDataDiv):
        reserved = False
        reservedElement = propertyDataDiv.find(
            "div", {"data-qa": "POSTING_CARD_GALLERY"}
        )
        reservedElement = reservedElement.find_all("div")

        for div in reservedElement:
            spanElement = div.find_all("span")
            for span in spanElement:
                if "Reservado" in span.get_text():
                    reserved = True

        return reserved

    @_getPropertyData
    def getPropertiesProvider(self, propertyDataDiv):
        provider = "Zonaprop"

        return provider

    @_getPropertyData
    def getPropertiesDownloadDate(self, propertyDataDiv):
        formatString = "%Y-%m-%d %H:%M:%S"
        downloadedTime = time.strftime(formatString, time.localtime())

        return downloadedTime

    def _forAreaStripMeasureAndConvertToInteger(self, propertyAreaAttribute, mesure):
        if pd.isna(propertyAreaAttribute):
            return propertyAreaAttribute
        else:
            return int(propertyAreaAttribute.strip(mesure))

    def _getPropertyAttributes(self, data):
        propertyAttributes = data.find("h3", {"data-qa": "POSTING_CARD_FEATURES"})

        if propertyAttributes is None:
            return propertyAttributes

        propertyAttributes = propertyAttributes.find_all("span")
        return propertyAttributes

    def _findPropertyAttributes(self, data, attributeName):
        propertyAttributes = []

        if data is None:
            return pd.NA

        self._forSpanInDataFindAllTheAttributesWith(
            data, attributeName, propertyAttributes
        )

        if propertyAttributes:
            return propertyAttributes[0]

        return pd.NA

    def _forSpanInDataFindAllTheAttributesWith(
        self, data, attributeName, propertyAttributes
    ):
        for span in data:
            if attributeName in span.get_text():
                propertyAttributes.append(str(span.get_text().strip()))

    def _propertyAttributesLogger(self, func, res):
        if pd.isna(res):
            logging.warning(
                f"Property attribute data from {self.url} is NaN using {func.__name__}."
            )
        else:
            logging.info(
                f"Property attribute data from {self.url} is found using {func.__name__}."
            )
