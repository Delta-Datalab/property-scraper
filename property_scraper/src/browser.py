import cloudscraper


class Browser:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def fetch_page(self, url):
        response = self.scraper.get(url)
        if response.status_code == 200:
            return response.text
        return None
