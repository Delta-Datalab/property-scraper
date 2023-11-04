from src.browser import Browser
from bs4 import BeautifulSoup
from src.property import Property, ZonaPropProperty
from config import LOG_DIR

import logging
import pandas as pd
import os

os.path.exists(LOG_DIR) or open(LOG_DIR, 'w').close()
logging.basicConfig(filename=LOG_DIR, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Scraper:
    def __init__(self, browser):
        self.browser = browser

    def scrape_data_properties_to_df(self, url):
        try:
            logging.info(f"Starting to scrape the data property and storage to a dataframe")
            data = self.browser.fetch_page(url)
            
            soup = BeautifulSoup(data, 'html.parser')
            data_qa_divs = soup.find_all('div', {'data-posting-type': 'PROPERTY'})
            
            propiedades = []
            tipo_propiedad = ZonaPropProperty()
            
            for data_container in data_qa_divs:
                propiedades.append(Property(tipo_propiedad,data_container))
                
            df = pd.DataFrame(columns=['price'])
            
            for propiedad in propiedades:
                df.loc[len(df.index)] = [propiedad.get_price()]
            
            df.to_csv("data.csv")
            logging.info(f"Successfully scrape the data property and storage to a dataframe")
        except Exception as e:
            logging.error(f"Error scraping the property data: {e}")
            return
