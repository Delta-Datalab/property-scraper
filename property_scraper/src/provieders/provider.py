import pandas as pd


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
