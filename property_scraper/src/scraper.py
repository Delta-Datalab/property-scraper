from src.browser import Browser
from bs4 import BeautifulSoup
from src.provieder import Provieder
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
            provieder_type = PropertyParser.get_propertyType(domain)
            
            provieder = Provieder(parsed_data, provieder_type)

            df = provieder.getDataFromProperties()

            df.to_csv(OUTPUT_DATA_DIR)
            logging.info(
                f"Successfully scrape the data property and storage to a dataframe"
            )
        except Exception as e:
            logging.error(f"Error scraping the property data: {e}")
            return
