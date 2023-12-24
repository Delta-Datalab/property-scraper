import pandas as pd


class Provider:
    def __init__(self, provider_data):
        self.data = provider_data
        self.properties = []

    def getDataFromProperties(self):
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

        propertiesDataframe = pd.DataFrame(
            columns=[
                "url",
                "price",
                "currency",
                "expenses",
                "expenses_currency",
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

    def getNextPageURL(self):
        """
        Retrieves the URL of the next page.

        Returns:
            str: The URL of the next page.
        """
        pass