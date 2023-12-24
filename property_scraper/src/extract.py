from src.browser import Browser
from src.scraper import Scraper


class Extract:
    def download_data(self, url):
        """Downloads data from the specified URL.

        Args:
            url (str): The URL from which to download the data.
        """

        browser = Browser()
        scraper = Scraper(browser)

        scraper.exportPropertiesDataToCSV(url)
