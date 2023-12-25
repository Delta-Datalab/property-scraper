import pytest
import os
from bs4 import BeautifulSoup

from src.providers.zonaprop import zonapropProvider
from src.providerFactory import ProviderFactory


@pytest.fixture
def fixture_data():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


def test_validateProviderFactoryGivesCorrectProviderSubclass(fixture_data):
    url = "https://www.zonaprop.com.ar/"
    provider = ProviderFactory().create_provider(url, fixture_data)

    assert isinstance(provider, zonapropProvider)


def test_validateProviderFactoryRaiseAnErrorWhenProvideInvalidProviderURL(fixture_data):
    url = "https://www.invalidprovider.com/"
    with pytest.raises(ValueError):
        ProviderFactory().create_provider(url, fixture_data)
