import numpy as np
import logging

from urllib.parse import urlparse
from src.providers.zonaprop import zonapropProvider


class ProviderFactory:
    @classmethod
    def createProvider(cls, url, providerData):
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
            provider = zonapropProvider(providerData, url)
        else:
            logging.error(f"Invalid type of Provider")
            raise ValueError("Invalid type of Provider")

        return provider
