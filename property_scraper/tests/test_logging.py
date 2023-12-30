import os
import pytest
import logging

from src.providers.zonaprop import *
from bs4 import BeautifulSoup
from collections import Counter
from tests.fixtures.zonapropExpectedLogs import *


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

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesPrices")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesPrices")

    assert logCounts[expectFoundLogMessage] == expectedLogsCount
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyOneWithNoPrice(fixture_data_no_price, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data_no_price, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.WARNING)
    provider.getPropertiesPrices()

    logCounts = Counter(caplog.messages)

    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesPrices")

    assert logCounts[expectNaNLogMessage] == 1

def test_validateLoggingPropertyExpenses(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesExpenses()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesExpenses")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesExpenses")

    assert logCounts[expectFoundLogMessage] == 18
    assert logCounts[expectNaNLogMessage] == 2

def test_validateLoggingPropertyBathrooms(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesBathrooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesBathrooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesBathrooms")

    assert logCounts[expectFoundLogMessage] == 19
    assert logCounts[expectNaNLogMessage] == 1

def test_validateLoggingPropertyBedrooms(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesBedrooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesBedrooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesBedrooms")

    assert logCounts[expectFoundLogMessage] == 18
    assert logCounts[expectNaNLogMessage] == 2

def test_validateLoggingPropertyTotalRooms(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesTotalRooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesTotalRooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesTotalRooms")

    assert logCounts[expectFoundLogMessage] == 19
    assert logCounts[expectNaNLogMessage] == 1

def test_validateLoggingPropertyCoveredAreas(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesCoveredAreas()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesCoveredAreas")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesCoveredAreas")

    assert logCounts[expectFoundLogMessage] == 19
    assert logCounts[expectNaNLogMessage] == 1

def test_validateLoggingPropertyTotalAreas(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesTotalAreas()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesTotalAreas")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesTotalAreas")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0

def test_validateLoggingPropertyCurrencies(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesCurrencies()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesCurrencies")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesCurrencies")

    assert logCounts[expectFoundLogMessage] == 9
    assert logCounts[expectNaNLogMessage] == 11

def test_validateLoggingPropertyDescriptions(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesDescriptions()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesDescriptions")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesDescriptions")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0

def test_validateLoggingPropertyParkings(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesParkings()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesParkings")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesParkings")

    assert logCounts[expectFoundLogMessage] == 9
    assert logCounts[expectNaNLogMessage] == 11

def test_validateLoggingPropertyURLs(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesURLs()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesURLs")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesURLs")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0

def test_validateLoggingPropertyLocations(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesLocations()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesLocations")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesLocations")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0

def test_validateLoggingPropertyRealStateAgencies(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesRealStateAgencies()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesRealStateAgencies")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesRealStateAgencies")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0

def test_validateLoggingPropertyReserved(fixture_data, caplog):
    caplog.clear()
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesReserved()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesReserved")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesReserved")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0