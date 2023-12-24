import cloudscraper


class Browser:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def fetch_page(self, url):
        """
        Fetches the content of a web page given its URL.

        Args:
            url (str): The URL of the web page to fetch.

        Returns:
            str or None: The content of the web page as a string if the request is successful,
                         None otherwise.
        """
        response = self.scraper.get(url)
        if response.status_code == 200:
            return response.text
        return None
