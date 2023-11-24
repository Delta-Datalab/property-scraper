import os
import numpy as np
import pytest

from src.browser import Browser
from src.scraper import Scraper
from bs4 import BeautifulSoup

from unittest.mock import MagicMock

    
@pytest.fixture
def fixture_data():
    fixture_directory = os.path.join(os.getcwd(), 'tests', 'fixtures', 'zonapropFixture.html')
    with open(fixture_directory, 'r') as file:
        html_content = file.read()
    return BeautifulSoup(html_content, 'html.parser')

@pytest.fixture
def scraper():
    return Scraper(Browser())

    
def test_validatePropertyPrices(fixture_data, scraper):
    properties_prices_data = scraper.getPricesFromPropertiesData(fixture_data).values
    
    expected_data = np.array([
        ['Consultar precio'],['Consultar precio'], ['$ 200.000'],['Consultar precio'],['Consultar precio'],
        ['Consultar precio'],['$ 350.000'],['$ 400.000'],['$ 380.000'],['Consultar precio'],
        ['Consultar precio'],['Consultar precio'],['$ 370.000'],['$ 350.000'],['Consultar precio'],
        ['Consultar precio'],['$ 230.000'],['Consultar precio'],['$ 400.000'],['$ 380.000']
    ])
    
    assert np.array_equal(properties_prices_data, expected_data)