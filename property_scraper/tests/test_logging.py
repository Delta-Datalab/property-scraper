import os
import pytest
import logging

from src.providers.zonaprop import *
from bs4 import BeautifulSoup
from collections import Counter
from tests.fixtures.zonapropExpectedLogs import *


@pytest.fixture
def fixtureData():
    fixtureDirectory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture_4.html"
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")



def test_validateLoggingPropertyPrices(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesPrices()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesPrices")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesPrices")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyExpenses(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesExpenses()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesExpenses")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesExpenses")

    assert logCounts[expectFoundLogMessage] == 14
    assert logCounts[expectNaNLogMessage] == 6


def test_validateLoggingPropertyExpensesCurrencies(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    res = provider.getPropertiesExpensesCurrencies()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesExpensesCurrencies")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesExpensesCurrencies")

    assert logCounts[expectFoundLogMessage] == 14
    assert logCounts[expectNaNLogMessage] == 6


def test_validateLoggingPropertyBathrooms(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesBathrooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesBathrooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesBathrooms")

    assert logCounts[expectFoundLogMessage] == 18
    assert logCounts[expectNaNLogMessage] == 2


def test_validateLoggingPropertyBedrooms(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesBedrooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesBedrooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesBedrooms")

    assert logCounts[expectFoundLogMessage] == 18
    assert logCounts[expectNaNLogMessage] == 2


def test_validateLoggingPropertyTotalRooms(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesTotalRooms()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesTotalRooms")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesTotalRooms")

    assert logCounts[expectFoundLogMessage] == 18
    assert logCounts[expectNaNLogMessage] == 2


def test_validateLoggingPropertyCoveredAreas(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesCoveredAreas()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesCoveredAreas")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesCoveredAreas")

    assert logCounts[expectFoundLogMessage] == 0
    assert logCounts[expectNaNLogMessage] == 20


def test_validateLoggingPropertyTotalAreas(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesTotalAreas()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesTotalAreas")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesTotalAreas")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyCurrencies(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesCurrencies()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesCurrencies")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesCurrencies")

    assert logCounts[expectFoundLogMessage] == 19
    assert logCounts[expectNaNLogMessage] == 1


def test_validateLoggingPropertyDescriptions(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesDescriptions()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesDescriptions")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesDescriptions")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyParkings(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesParkings()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesParkings")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesParkings")

    assert logCounts[expectFoundLogMessage] == 5
    assert logCounts[expectNaNLogMessage] == 15


def test_validateLoggingPropertyURLs(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesURLs()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesURLs")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesURLs")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyLocations(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesLocations()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesLocations")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesLocations")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyRealStateAgencies(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesRealStateAgencies()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesRealStateAgencies")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesRealStateAgencies")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0


def test_validateLoggingPropertyReserved(fixtureData, caplog):
    caplog.clear()
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")

    caplog.set_level(logging.INFO)
    provider.getPropertiesReserved()

    logCounts = Counter(caplog.messages)

    expectFoundLogMessage = getExpectFoundLogMessage("getPropertiesReserved")
    expectNaNLogMessage = getExpectNanLogMessage("getPropertiesReserved")

    assert logCounts[expectFoundLogMessage] == 20
    assert logCounts[expectNaNLogMessage] == 0
