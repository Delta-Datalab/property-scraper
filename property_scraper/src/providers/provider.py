import pandas as pd
import logging


class Provider:
    def __init__(self, providerHTMLData):
        self.data = providerHTMLData

    def getDataFromProperties(self, aSubclassProvider):
        """
        Retrieves data from properties and returns it as a pandas DataFrame.

        Returns:
            pandas.DataFrame: A DataFrame containing the following columns:
            - url: The URL of the property.
            - price: The price of the property.
            - currency: The currency of the price.
            - expenses: The expenses associated with the property.
            - expenses_currency: The currency of the expenses.
            - location: The location of the property.
            - total_area: The total area of the property.
            - covered_area: The covered area of the property.
            - total_rooms: The total number of rooms in the property.
            - bathrooms: The number of bathrooms in the property.
            - bedrooms: The number of bedrooms in the property.
            - parking: The parking availability of the property.
            - real_state_agency: The real estate agency associated with the property.
            - reserved: The reservation status of the property.
            - description: The description of the property.
        """

        propertiesData = {
            "url": aSubclassProvider.getPropertiesURLs(),
            "provider": aSubclassProvider.getPropertiesProvider(),
            "price": aSubclassProvider.getPropertiesPrices(),
            "currency": aSubclassProvider.getPropertiesCurrencies(),
            "expenses": aSubclassProvider.getPropertiesExpenses(),
            "expenses_currency": aSubclassProvider.getPropertiesExpensesCurrencies(),
            "location": aSubclassProvider.getPropertiesLocations(),
            "total_area": aSubclassProvider.getPropertiesTotalAreas(),
            "covered_area": aSubclassProvider.getPropertiesCoveredAreas(),
            "total_rooms": aSubclassProvider.getPropertiesTotalRooms(),
            "bedrooms": aSubclassProvider.getPropertiesBedrooms(),
            "bathrooms": aSubclassProvider.getPropertiesBathrooms(),
            "reserved": aSubclassProvider.getPropertiesReserved(),
            "parking": aSubclassProvider.getPropertiesParkings(),
            "real_state_agency": aSubclassProvider.getPropertiesRealStateAgencies(),
            "download_date": aSubclassProvider.getPropertiesDownloadDate(),
            "description": aSubclassProvider.getPropertiesDescriptions(),
        }

        return pd.DataFrame(propertiesData)

    def getNextPageURL(self):
        """
        Retrieves the URL of the next page.

        Returns:
            str: The URL of the next page.
        """
        pass

    def getPropertiesPrices(self, propertyDataDiv):
        """
        Retrieves the prices of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The price of the property.
        """
        pass

    def getPropertiesExpenses(self, propertyDataDiv):
        """
        Retrieves the expenses of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The expenses of the property.
        """
        pass

    def getPropertiesExpensesCurrencies(self, propertyDataDiv):
        """
        Retrieves the expenses currencies of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The expenses currency of the property.
        """
        pass

    def getPropertiesBathrooms(self, propertyDataDiv):
        """
        Retrieves the bathrooms of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The bathrooms of the property.
        """
        pass

    def getPropertiesBedrooms(self, propertyDataDiv):
        """
        Retrieves the bedrooms of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The bedrooms of the property.
        """
        pass

    def getPropertiesTotalRooms(self, propertyDataDiv):
        """
        Retrieves the total rooms of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The total rooms of the property.
        """
        pass

    def getPropertiesCoveredAreas(self, propertyDataDiv):
        """
        Retrieves the covered areas of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The covered areas of the property.
        """
        pass

    def getPropertiesTotalAreas(self, propertyDataDiv):
        """
        Retrieves the total areas of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The total areas of the property.
        """
        pass

    def getPropertiesCurrencies(self, propertyDataDiv):
        """
        Retrieves the currencies of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The currencies of the property.
        """
        pass

    def getPropertiesDescriptions(self, propertyDataDiv):
        """
        Retrieves the descriptions of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The descriptions of the property.
        """
        pass

    def getPropertiesParkings(self, propertyDataDiv):
        """
        Retrieves the parking of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The parking of the property.
        """
        pass

    def getPropertiesURLs(self, propertyDataDiv):
        """
        Retrieves the URLs of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The URLs of the property.
        """
        pass

    def getPropertiesLocations(self, propertyDataDiv):
        """
        Retrieves the locations of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The locations of the property.
        """
        pass

    def getPropertiesRealStateAgencies(self, propertyDataDiv):
        """
        Retrieves the real state agencies of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            bool: The real state agencies of the property.
        """
        pass

    def getPropertiesReserved(self, propertyDataDiv):
        """
        Retrieves the reserved status of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            bool: The reserved status of the property.
        """
        pass

    def getProviderFromFixtureData(self, propertyDataDiv):
        """
        Retrieves the providers of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The property provider.
        """
        pass

    def getDownloadDateFromFixtureData(self, propertyDataDiv):
        """
        Retrieves the download date of the properties.

        Args:
            propertyDataDiv (bs4.element.Tag): The div containing the property data.

        Returns:
            str: The downloaded date for the property.
        """
        pass
