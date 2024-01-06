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
def fixture_data():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


@pytest.fixture
def fixture_description_data():
    fixture_directory = os.path.join(
        os.getcwd(), "tests", "fixtures", "zonapropFixture_2.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


@pytest.fixture
def fixture_real_state_agency_and_reserved_data():
    fixture_directory = os.path.join(
        os.getcwd(),
        "tests",
        "fixtures",
        "zonapropFixture_realStateAgencyAndReserved.html",
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


def test_validatePropertyPrices(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_prices_data = provider.getPropertiesPrices()

    expected_prices = getPricesFromFixtureData()

    pd.testing.assert_series_equal(properties_prices_data, expected_prices)


def test_validatePropertyExpenses(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_expenses_data = provider.getPropertiesExpenses()

    expected_expenses = getExpensesFromFixtureData()

    pd.testing.assert_series_equal(properties_expenses_data, expected_expenses)


def test_validatePropertyExpensesCurrency(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_expenses_currency_data = provider.getPropertiesExpensesCurrencies()

    expected_expenses_currency = getExpensesCurrencyFromFixtureData()

    pd.testing.assert_series_equal(
        properties_expenses_currency_data, expected_expenses_currency
    )


def test_validatePropertyBathrooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_bathroom_data = provider.getPropertiesBathrooms()

    expected_bathrooms = getBathroomsFromFixtureData()

    pd.testing.assert_series_equal(properties_bathroom_data, expected_bathrooms)


def test_validatePropertyBedrooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_bedrooms_data = provider.getPropertiesBedrooms()

    expected_bedrooms = getBedroomsFromFixtureData()

    pd.testing.assert_series_equal(properties_bedrooms_data, expected_bedrooms)


def test_validatePropertyTotalRooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_total_rooms_data = provider.getPropertiesTotalRooms()

    expected_total_rooms = getTotalRoomsFromFixtureData()

    pd.testing.assert_series_equal(properties_total_rooms_data, expected_total_rooms)


def test_validatePropertyCoveredArea(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_covered_area_data = provider.getPropertiesCoveredAreas()

    expected_covered_area = getCoveredAreaFromFixtureData()

    pd.testing.assert_series_equal(properties_covered_area_data, expected_covered_area)


def test_validatePropertyTotalArea(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_total_area_data = provider.getPropertiesTotalAreas()

    expected_total_area = getTotalAreaFromFixtureData()

    pd.testing.assert_series_equal(properties_total_area_data, expected_total_area)


def test_validatePropertyDescription(fixture_description_data):
    provider = zonapropProvider(
        fixture_description_data, "https://www.zonaprop.com.ar/"
    )
    properties_description_data = provider.getPropertiesDescriptions()

    expected_description = getDescriptionFromFixtureData()

    pd.testing.assert_series_equal(properties_description_data, expected_description)


def test_validatePropertyParking(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_parking_data = provider.getPropertiesParkings()

    expected_parking = getParkingFromFixtureData()

    pd.testing.assert_series_equal(properties_parking_data, expected_parking)


def test_validatePropertyCurrency(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_currency_data = provider.getPropertiesCurrencies()

    expected_currency = getCurrencyFromFixtureData()
    pd.testing.assert_series_equal(properties_currency_data, expected_currency)


def test_validatePropertyUrl(fixture_description_data):
    provider = zonapropProvider(
        fixture_description_data, "https://www.zonaprop.com.ar/"
    )
    properties_url_data = provider.getPropertiesURLs()

    expected_url = getUrlFromFixtureData()
    pd.testing.assert_series_equal(properties_url_data, expected_url)


def test_validatePropertyLocation(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_location_data = provider.getPropertiesLocations()

    expected_location = getLocationFromFixtureData()

    pd.testing.assert_series_equal(properties_location_data, expected_location)


def test_validateRealStateAgency(fixture_real_state_agency_and_reserved_data):
    provider = zonapropProvider(
        fixture_real_state_agency_and_reserved_data, "https://www.zonaprop.com.ar/"
    )
    properties_real_state_agency_data = provider.getPropertiesRealStateAgencies()

    expected_real_state_agency = getRealStateAgencyFromFixtureData()

    pd.testing.assert_series_equal(
        properties_real_state_agency_data, expected_real_state_agency
    )


def test_validatePropertyReserved(fixture_real_state_agency_and_reserved_data):
    provider = zonapropProvider(
        fixture_real_state_agency_and_reserved_data, "https://www.zonaprop.com.ar/"
    )
    properties_reserved_properties_data = provider.getPropertiesReserved()

    expected_reserved_properties = getReservedPropertiesFromFixtureData()

    pd.testing.assert_series_equal(
        properties_reserved_properties_data, expected_reserved_properties
    )


def test_getNextPageURLWhenPageIsNotPresent(fixture_data):
    provider = zonapropProvider(
        fixture_data, "https://www.zonaprop.com.ar/departamentos-alquiler-palermo.html"
    )

    # Test when "pagina-" is not present in the URL
    assert (
        provider.getNextPageURL()
        == "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-2.html"
    )


def test_getNextPageURLWhenPageIsPresent(fixture_data):
    provider = zonapropProvider(
        fixture_data,
        "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-2.html",
    )

    # Test when "pagina-" is present in the URL
    assert (
        provider.getNextPageURL()
        == "https://www.zonaprop.com.ar/departamentos-alquiler-palermo-pagina-3.html"
    )


def test_validatePropertyProviderType(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    propertiesTypeData = provider.getPropertiesProvider()

    expectedProvider = getProviderFromFixtureData()

    pd.testing.assert_series_equal(propertiesTypeData, expectedProvider)


@freeze_time("2000-01-01 12:00:00")
def test_validateDownloadDate(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    propertiesTypeData = provider.getPropertiesDownloadDate()

    expectedDownloadDate = getDownloadDateFromFixtureData()

    pd.testing.assert_series_equal(propertiesTypeData, expectedDownloadDate)
