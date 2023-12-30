from bs4 import BeautifulSoup
from src.providerFactory import ProviderFactory
from datetime import datetime
from config import *

import os
import logging


class Scraper:
    def __init__(self, browser):
        self.browser = browser
        self.procesedProviderURLs = []

    def exportPropertiesDataToCSV(self, url):
        """Scrapes the data property from the given URL and stores it in a dataframe.

        Args:
            url (str): The URL of the webpage to scrape.

        Returns:
            None
        """

        try:
            logging.info(
                f"Starting to scrape the data property from {url} and storage to a dataframe"
            )
            response = self.browser.fetch_page(url)
            if self._assertResponseIsInvalid(response):
                return
            self.procesedProviderURLs.append(response.url)
            provider = self.getProvider(response)

            propertyDataDataFrame = provider.getDataFromProperties()

            self.exportPropertyDataToCSV(propertyDataDataFrame)
            logging.info(
                f"Successfully scrape the data property from {url} and storage to a dataframe"
            )
            self.exportPropertiesDataToCSV(provider.getNextPageURL())
        except Exception as e:
            logging.error(f"Error scraping the property data from {url}: {e}")
            return

    def _assertResponseIsInvalid(self, response):
        if self._assertURLisProcessed(response):
            logging.info(f"Succesfully scrape the data property from all pages")
            return True
        return response == None

    def _assertURLisProcessed(self, response):
        response.url = response.url.replace(":443", "")
        return response.url in self.procesedProviderURLs

    def getProvider(self, response):
        """
        Retrieves the provider for the given URL.

        Args:
            url (str): The URL to fetch the provider from.

        Returns:
            Provider: The provider object for the given URL.
        """
        data = response.text
        parsedData = BeautifulSoup(data, "html.parser")

        provider = ProviderFactory.create_provider(response.url, parsedData)
        return provider

    def exportPropertyDataToCSV(self, propertyData):
        """Exports the property data to a CSV file.

        Args:
            propertyData (DataFrame): The property data to export.

        Returns:
            None
        """

        logging.info(f"Starting to export the property data to a CSV file")
        filename = self._getDataCSVName()
        outputDataDir = os.path.join(DATA_DIR, filename)
        propertyData.to_csv(outputDataDir)
        logging.info(f"Successfully exported the property data to a CSV file")

    def _getDataCSVName(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")
        filename = "property_data-" + formatted_datetime + ".csv"
        return filename
