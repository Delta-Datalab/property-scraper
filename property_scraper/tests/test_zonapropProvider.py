import os
import numpy as np
import pytest
import pandas as pd

from src.browser import Browser
from src.scraper import Scraper
from src.providers.zonaprop import zonapropProvider
from tests.fixtures.zonapropExpectedData import *
from bs4 import BeautifulSoup
from freezegun import freeze_time


@pytest.fixture
def fixtureData():
    fixtureDirectory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture_4.html"
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")


@pytest.fixture
def fixtureDescriptionData():
    fixtureDirectory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture_Description.html"
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")


@pytest.fixture
def fixtureRealStateAgencyData():
    fixtureDirectory = os.path.join(
        os.getcwd(),
        "tests",
        "fixtures",
        "zonapropFixture_realStateAgency.html",
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")


@pytest.fixture
def fixtureReservedData():
    fixtureDirectory = os.path.join(
        os.getcwd(),
        "tests",
        "fixtures",
        "zonapropFixture_reserved.html",
    )
    with open(fixtureDirectory, "r") as file:
        htmlContent = file.read()
    return BeautifulSoup(htmlContent, "html.parser")


def test_validatePropertyPrices(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesPricesData = provider.getPropertiesPrices()

    expectedPrices = getPricesFromFixtureData()

    pd.testing.assert_series_equal(propertiesPricesData, expectedPrices)


def test_validatePropertyExpenses(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesExpensesData = provider.getPropertiesExpenses()

    expectedExpenses = getExpensesFromFixtureData()

    pd.testing.assert_series_equal(propertiesExpensesData, expectedExpenses)


def test_validatePropertyExpensesCurrency(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesExpensesCurrencyData = provider.getPropertiesExpensesCurrencies()

    expectedExpensesCurrency = getExpensesCurrencyFromFixtureData()

    pd.testing.assert_series_equal(
        propertiesExpensesCurrencyData, expectedExpensesCurrency
    )


def test_validatePropertyBathrooms(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesBathroomData = provider.getPropertiesBathrooms()

    expectedBathrooms = getBathroomsFromFixtureData()

    pd.testing.assert_series_equal(propertiesBathroomData, expectedBathrooms)


def test_validatePropertyBedrooms(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesBedroomsData = provider.getPropertiesBedrooms()

    expectedBedrooms = getBedroomsFromFixtureData()

    pd.testing.assert_series_equal(propertiesBedroomsData, expectedBedrooms)


def test_validatePropertyTotalRooms(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesTotalRoomsData = provider.getPropertiesTotalRooms()

    expectedTotalRooms = getTotalRoomsFromFixtureData()

    pd.testing.assert_series_equal(propertiesTotalRoomsData, expectedTotalRooms)


def test_validatePropertyCoveredArea(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesCoveredAreaData = provider.getPropertiesCoveredAreas()

    expectedCoveredArea = getCoveredAreaFromFixtureData()

    pd.testing.assert_series_equal(propertiesCoveredAreaData, expectedCoveredArea)


def test_validatePropertyTotalArea(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesTotalAreaData = provider.getPropertiesTotalAreas()

    expectedTotalArea = getTotalAreaFromFixtureData()

    pd.testing.assert_series_equal(propertiesTotalAreaData, expectedTotalArea)


def test_validatePropertyDescription(fixtureDescriptionData):
    provider = zonapropProvider(fixtureDescriptionData, "https://www.zonaprop.com.ar/")
    propertiesDescriptionData = provider.getPropertiesDescriptions()
    
    expectedDescription = getDescriptionFromFixtureData()

    pd.testing.assert_series_equal(propertiesDescriptionData, expectedDescription)


def test_validatePropertyParking(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesParkingData = provider.getPropertiesParkings()

    expectedParking = getParkingFromFixtureData()

    pd.testing.assert_series_equal(propertiesParkingData, expectedParking)


def test_validatePropertyCurrency(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesCurrencyData = provider.getPropertiesCurrencies()

    expectedCurrency = getCurrencyFromFixtureData()
    pd.testing.assert_series_equal(propertiesCurrencyData, expectedCurrency)


def test_validatePropertyUrl(fixtureDescriptionData):
    provider = zonapropProvider(fixtureDescriptionData, "https://www.zonaprop.com.ar/")
    propertiesUrlData = provider.getPropertiesURLs()

    expectedUrl = getUrlFromFixtureData()
    pd.testing.assert_series_equal(propertiesUrlData, expectedUrl)


def test_validatePropertyLocation(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesLocationData = provider.getPropertiesLocations()

    expectedLocation = getLocationFromFixtureData()

    pd.testing.assert_series_equal(propertiesLocationData, expectedLocation)


def test_validateRealStateAgency(fixtureRealStateAgencyData):
    provider = zonapropProvider(
        fixtureRealStateAgencyData, "https://www.zonaprop.com.ar/"
    )
    propertiesRealStateAgencyData = provider.getPropertiesRealStateAgencies()

    expectedRealStateAgency = getRealStateAgencyFromFixtureData()

    pd.testing.assert_series_equal(
        propertiesRealStateAgencyData, expectedRealStateAgency
    )


def test_validatePropertyReserved(fixtureReservedData):
    provider = zonapropProvider(
        fixtureReservedData, "https://www.zonaprop.com.ar/"
    )
    propertiesReservedPropertiesData = provider.getPropertiesReserved()

    expectedReservedProperties = getReservedPropertiesFromFixtureData()

    pd.testing.assert_series_equal(
        propertiesReservedPropertiesData, expectedReservedProperties
    )


def test_getNextPageURLWhenPageIsNotPresent(fixtureData):
    provider = zonapropProvider(
        fixtureData, "https://www.zonaprop.com.ar/departamentos-alquiler-palermo.html"
    )

    # Test when "pagina-" is not present in the URL
    assert (
        provider.getNextPageURL()
        == "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-2.html"
    )


def test_getNextPageURLWhenPageIsPresent(fixtureData):
    provider = zonapropProvider(
        fixtureData,
        "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-2.html",
    )

    # Test when "pagina-" is present in the URL
    assert (
        provider.getNextPageURL()
        == "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-3.html"
    )


def test_validatePropertyProviderType(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesTypeData = provider.getPropertiesProvider()

    expectedProvider = getProviderFromFixtureData()

    pd.testing.assert_series_equal(propertiesTypeData, expectedProvider)


@freeze_time("2000-01-01 12:00:00")
def test_validateDownloadDate(fixtureData):
    provider = zonapropProvider(fixtureData, "https://www.zonaprop.com.ar/")
    propertiesTypeData = provider.getPropertiesDownloadDate()

    expectedDownloadDate = getDownloadDateFromFixtureData()

    pd.testing.assert_series_equal(propertiesTypeData, expectedDownloadDate)

