from src.browser import Browser
from bs4 import BeautifulSoup
from src.property import Property, ZonaPropProperty

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

os.path.exists(LOG_DIR) or open(LOG_DIR, 'w').close()
logging.basicConfig(filename=LOG_DIR, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Scraper:
    def __init__(self, browser):
        self.browser = browser

    def scrape_data_properties_to_df(self, url):
        try:
            logging.info(f"Starting to scrape the data property and storage to a dataframe")
            data = self.browser.fetch_page(url)
            parsed_data = BeautifulSoup(data, 'html.parser')

            domain = urlparse(url).netloc
            
            df = self.getPricesFromProperties(parsed_data, domain)
            
            df.to_csv(OUTPUT_DATA_DIR)
            logging.info(f"Successfully scrape the data property and storage to a dataframe")
        except Exception as e:
            logging.error(f"Error scraping the property data: {e}")
            return

    def getPricesFromProperties(self, data, domain):
        data_qa_divs = data.find_all('div', {'data-posting-type': 'PROPERTY'})
            
        propiedades = []
            
        for data_container in data_qa_divs:
            propiedades.append(Property(data_container,domain))
                
        df = pd.DataFrame(columns=['price'])
            
        for propiedad in propiedades:
            df.loc[len(df.index)] = [propiedad.get_price()]
            
        return df

    def getExpensesFromProperties(self, data, domain):
        data_qa_divs = data.find_all('div', {'data-posting-type': 'PROPERTY'})
            
        propiedades = []
            
        for data_container in data_qa_divs:
            propiedades.append(Property(data_container,domain))
                
        df = pd.DataFrame(columns=['expenses'])
            
        for propiedad in propiedades:
            df.loc[len(df.index)] = [propiedad.get_expenses()]
            
        return df