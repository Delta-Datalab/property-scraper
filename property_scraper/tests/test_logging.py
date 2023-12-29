import os
import pytest
import logging

from src.providers.zonaprop import *
from bs4 import BeautifulSoup
from collections import Counter


@pytest.fixture
def fixture_data():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


@pytest.fixture
def fixture_data_no_price():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture_3.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


def test_validateLoggingPropertyPrices(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesPrices()

    logCounts = Counter(caplog.messages)
    expectedLogsCount = 20

    expectScrappingLogMessage = "Scraping property attribute data from https://www.zonaprop.com.ar/ using getPropertiesPrices."
    expectFoundLogMessage = "Property attribute data from https://www.zonaprop.com.ar/ is found using getPropertiesPrices."
    expectNaNLogMessage = "Property attribute data from https://www.zonaprop.com.ar/ is NaN using getPropertiesPrices."

    assert logCounts[expectScrappingLogMessage] == expectedLogsCount
    assert logCounts[expectFoundLogMessage] == expectedLogsCount
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyOneWithNoPrice(fixture_data_no_price, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data_no_price, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.WARNING)
    provider.getPropertiesPrices()

    logCounts = Counter(caplog.messages)

    expectNaNLogMessage = "Property attribute data from https://www.zonaprop.com.ar/ is NaN using getPropertiesPrices."

    assert logCounts[expectNaNLogMessage] == 1
