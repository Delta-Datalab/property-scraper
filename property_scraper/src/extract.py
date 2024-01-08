from src.browser import Browser
from src.scraper import Scraper


class Extract:
    def downloadData(self, url, mergeOutputDataFlag):
        """Downloads data from the specified URL.

        Args:
            url (str): The URL from which to download the data.
        """

        browser = Browser()
        scraper = Scraper(browser, mergeOutputDataFlag)

        scraper.exportPropertiesDataToCSV(url)
