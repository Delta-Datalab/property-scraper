from bs4 import BeautifulSoup
from src.providerFactory import ProviderFactory
from datetime import datetime
from config import *

import os
import logging


class Scraper:
    def __init__(self, browser, merge_output_data):
        self.browser = browser
        self.procesedProviderURLs = []
        self.mergeOutputData = merge_output_data
        self.outputDataPath = None  

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

            if self._assertNoNewFileNedded():
                self.exportPropertyDataToUniqueCSV(propertyDataDataFrame)
            else:
                self.exportPropertyDataToNewCSV(propertyDataDataFrame)
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
    
    def _assertNoNewFileNedded(self):
        return self.mergeOutputData and self.outputDataPath is not None

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

    def exportPropertyDataToUniqueCSV(self, propertyData):
        """Exports the property data to an existing CSV file.

        Args:
            propertyData (DataFrame): The property data to export.

        Returns:
            None
        """
        
        logging.info(f"Starting to export the property data to {self.outputDataPath} file")
        propertyData.to_csv(self.outputDataPath, mode='a', header=False, index = False)
        logging.info(f"Successfully exported the property data to {self.outputDataPath} file")

    def exportPropertyDataToNewCSV(self, propertyData):
        """Exports the property data to a CSV file.

        Args:
            propertyData (DataFrame): The property data to export.

        Returns:
            None
        """

        logging.info(f"Starting to export the property data to a CSV file")
        filename = self._getDataCSVName()
        outputDataDir = os.path.join(DATA_DIR, filename)
        if self.mergeOutputData:
            self.outputDataPath = outputDataDir
        propertyData.to_csv(outputDataDir, index = False)
        logging.info(f"Successfully exported the property data to a CSV file")

    def _getDataCSVName(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H:%M:%S")
        filename = "property_data-" + formatted_datetime + ".csv"
        return filename
