from src.browser import Browser
from src.scraper import Scraper

class Extract:
    
    def download_data(self, url):
        browser = Browser()
        scraper = Scraper(browser)
        
        scraper.scrape_data_properties_to_df(url)