from src.browser import Browser
from bs4 import BeautifulSoup
from src.property import Property, ZonaPropProperty
from src.propertyParser import PropertyParser

from config import LOG_DIR
from config import OUTPUT_DATA_DIR

import logging
import pandas as pd
import os
import numpy as np
from urllib.parse import urlparse

log_directory = os.path.dirname(LOG_DIR)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

os.path.exists(LOG_DIR) or open(LOG_DIR, "w").close()
logging.basicConfig(
    filename=LOG_DIR,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Scraper:
    def __init__(self, browser):
        self.browser = browser

    def scrape_data_properties_to_df(self, url):
        """Scrapes the data property from the given URL and stores it in a dataframe.

        Args:
            url (str): The URL of the webpage to scrape.

        Returns:
            None
        """

        try:
            logging.info(
                f"Starting to scrape the data property and storage to a dataframe"
            )
            data = self.browser.fetch_page(url)
            parsed_data = BeautifulSoup(data, "html.parser")

            domain = urlparse(url).netloc

            properties = self.getProperties(parsed_data, domain)
            df = self.getPricesFromProperties(properties)

            df.to_csv(OUTPUT_DATA_DIR)
            logging.info(
                f"Successfully scrape the data property and storage to a dataframe"
            )
        except Exception as e:
            logging.error(f"Error scraping the property data: {e}")
            return

    def getPricesFromProperties(self, properties):
        """Get prices from a list of properties.

        Args:
            properties (list): A list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the prices of the properties.
        """

        df = pd.DataFrame(columns=["price"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_price()]

        return df

    def getExpensesFromProperties(self, properties):
        """Get expenses from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the expenses for each property.
        """

        df = pd.DataFrame(columns=["expenses"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_expenses()]

        return df

    def getExpensesTypeFromProperties(self, properties):
        """Get expenses type from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the expenses type for each property.
        """

        df = pd.DataFrame(columns=["expenses_type"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_expenses_type()]

        return df

    def getBathroomsFromProperties(self, properties):
        """Get the number of bathrooms from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the number of bathrooms for each property.
        """

        df = pd.DataFrame(columns=["bathrooms"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_bathrooms()]

        return df

    def getBedroomsFromProperties(self, properties):
        """Get the number of bedrooms from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the number of bedrooms for each property.
        """

        df = pd.DataFrame(columns=["bedrooms"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_bedrooms()]

        return df

    def getTotalAreaFromProperties(self, properties):
        """Get total area from a list of properties.
        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the total area for each property.
        """

        df = pd.DataFrame(columns=["total_area"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_total_area()]

        return df

    def getCoveredAreaFromProperties(self, properties):
        """Get covered area from a list of properties.
        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the covered area for each property.
        """

        df = pd.DataFrame(columns=["covered_area"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_covered_area()]

        return df

    def getCurrencyFromProperties(self, properties):
        """Get the price currency from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the number of bathrooms for each property.
        """

        df = pd.DataFrame(columns=["currency"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_currency()]

        return df

    def getTotalRoomsFromProperties(self, properties):
        """Get the total number of rooms from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the total number of rooms for each property.
        """

        df = pd.DataFrame(columns=["total_rooms"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_total_rooms()]

        return df

    def getDescriptionFromProperties(self, properties):
        """Get the description from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the description for each property.
        """

        df = pd.DataFrame(columns=["description"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_description()]

        return df

    def getParkingFromProperties(self, properties):
        """Get parking from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the parking for each property.
        """

        df = pd.DataFrame(columns=["parking"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_parking()]

        return df

    def getUrlFromProperties(self, properties):
        """Get the URL from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the URL for each property.
        """

        df = pd.DataFrame(columns=["url"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_url()]

        return df

    def getLocationFromProperties(self, properties):
        """Get the location from a list of properties.

        Args:
            properties (list): The list of properties.

        Returns:
            pandas.DataFrame: A DataFrame containing the location for each property.
        """

        df = pd.DataFrame(columns=["location"])

        for property in properties:
            df.loc[len(df.index)] = [property.get_location()]

        return df

    def getProperties(self, data, domain):
        """Get properties from the given data and domain.

        Args:
            data (BeautifulSoup): The BeautifulSoup html.parser object containing the data.
            domain (str): The domain of the properties.

        Returns:
            list: A list of Property objects.
        """

        data_qa_divs = data.find_all("div", {"data-posting-type": "PROPERTY"})

        properties = []

        propertyParser = PropertyParser()
        property_type = propertyParser.get_propertyType(domain)

        for data_container in data_qa_divs:
            properties.append(Property(data_container, property_type))

        return properties
