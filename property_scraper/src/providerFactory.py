import numpy as np
import logging

from urllib.parse import urlparse
from src.providers.zonaprop import zonapropProvider


class ProviderFactory:
    @staticmethod
    def create_provider(url, provider_data):
        """
        Creates a provider object based on the given URL and provider data.

        Args:
            url (str): The URL of the provider.
            provider_data (dict): The data required to initialize the provider.

        Returns:
            object: An instance of the provider object.

        Raises:
            ValueError: If the URL is not supported.

        """
        parsedURL = urlparse(url).netloc
        if parsedURL == "www.zonaprop.com.ar":
            provider = zonapropProvider(provider_data, url)
        else:
            logging.error(f"Invalid type of Provider")
            raise ValueError("Invalid type of Provider")

        return provider
