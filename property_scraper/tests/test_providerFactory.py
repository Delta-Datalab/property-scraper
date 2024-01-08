import pytest
import os
from bs4 import BeautifulSoup

from src.providers.zonaprop import zonapropProvider
from src.providerFactory import ProviderFactory


@pytest.fixture
def fixtureData():
    fixtureDirectory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture.html"
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")


def test_validateProviderFactoryGivesCorrectProviderSubclass(fixtureData):
    url = "https://www.zonaprop.com.ar/"
    provider = ProviderFactory().createProvider(url, fixtureData)

    assert isinstance(provider, zonapropProvider)


def test_validateProviderFactoryRaiseAnErrorWhenProvideInvalidProviderURL(fixtureData):
    url = "https://www.invalidprovider.com/"
    with pytest.raises(ValueError):
        ProviderFactory().createProvider(url, fixtureData)
