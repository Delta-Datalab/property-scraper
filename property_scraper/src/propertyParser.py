import numpy as np

from src.provider import zonapropProvider


class ProviderFactory:
    @staticmethod
    def create_provider(url, provider_data):
        if url == "www.zonaprop.com.ar":
            provider = zonapropProvider(provider_data)
        else:
            raise ValueError("Invalid type of Provider")

        return provider
