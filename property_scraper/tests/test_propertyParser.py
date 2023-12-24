import pytest
import os
from bs4 import BeautifulSoup

from src.provieders.zonaprop import zonapropProvider
from src.propertyParser import ProviderFactory


@pytest.fixture
def fixture_data():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


def test_validatePropertyScraperGivesCorrectPropertyType(fixture_data):
    url = "www.zonaprop.com.ar"
    provider = ProviderFactory().create_provider(url, fixture_data)

    assert isinstance(provider, zonapropProvider)
