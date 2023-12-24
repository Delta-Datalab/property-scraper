from bs4 import BeautifulSoup
from src.propertyParser import ProviderFactory
from datetime import datetime
from urllib.parse import urlparse
from config import *

import logging
import os

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

    def exportPropertiesDataToCSV(self, url):
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
            provider = self.getProvider(url)

            propertyDataDataFrame = provider.getDataFromProperties()

            self.exportPropertyDataToCSV(propertyDataDataFrame)
            logging.info(
                f"Successfully scrape the data property and storage to a dataframe"
            )
        except Exception as e:
            logging.error(f"Error scraping the property data: {e}")
            return

    def getProvider(self, url):
        """
        Retrieves the provider for the given URL.

        Args:
            url (str): The URL to fetch the provider from.

        Returns:
            Provider: The provider object for the given URL.
        """
        data = self.browser.fetch_page(url)
        parsedData = BeautifulSoup(data, "html.parser")

        parsed_url = urlparse(url).netloc
        provider = ProviderFactory.create_provider(parsed_url, parsedData)
        return provider

    def exportPropertyDataToCSV(self, propertyData):
        """Exports the property data to a CSV file.

        Args:
            propertyData (DataFrame): The property data to export.

        Returns:
            None
        """
        try:
            logging.info(f"Starting to export the property data to a CSV file")
            filename = self._getDataCSVName()
            outputDataDir = os.path.dirname(DATA_DIR, filename)
            propertyData.to_csv(outputDataDir)
            logging.info(f"Successfully exported the property data to a CSV file")
        except Exception as e:
            logging.error(f"Error exporting the property data: {e}")
            return

    def _getDataCSVName(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        filename = "property_data" + formatted_datetime + ".csv"
        return filename
