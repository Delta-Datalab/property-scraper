from src.browser import Browser
from src.scraper import Scraper


class Extract:
    def downloadData(self, url, mergeOutputData):
        """Downloads data from the specified URL.

        Args:
            url (str): The URL from which to download the data.
        """

        browser = Browser()
        scraper = Scraper(browser, mergeOutputData)

        scraper.exportPropertiesDataToCSV(url)
