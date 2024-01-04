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
    properties_prices_data = provider.getDataFromProperties()["price"].to_frame()

    expected_prices = getPricesFromFixtureData()

    pd.testing.assert_frame_equal(properties_prices_data, expected_prices)


def test_validatePropertyExpenses(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_expenses_data = provider.getDataFromProperties()["expenses"].to_frame()

    expected_expenses = getExpensesFromFixtureData()

    pd.testing.assert_frame_equal(properties_expenses_data, expected_expenses)


def test_validatePropertyExpensesCurrency(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_expenses_currency_data = provider.getDataFromProperties()[
        "expenses_currency"
    ].to_frame()

    expected_expenses_currency = getExpensesCurrencyFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_expenses_currency_data, expected_expenses_currency
    )


def test_validatePropertyBathrooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_bathroom_data = provider.getDataFromProperties()["bathrooms"].to_frame()

    expected_bathrooms = getBathroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bathroom_data, expected_bathrooms)


def test_validatePropertyBedrooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_bedrooms_data = provider.getDataFromProperties()["bedrooms"].to_frame()

    expected_bedrooms = getBedroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bedrooms_data, expected_bedrooms)


def test_validatePropertyTotalRooms(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_total_rooms_data = provider.getDataFromProperties()[
        "total_rooms"
    ].to_frame()

    expected_total_rooms = getTotalRoomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_rooms_data, expected_total_rooms)


def test_validatePropertyCoveredArea(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_covered_area_data = provider.getDataFromProperties()[
        "covered_area"
    ].to_frame()

    expected_covered_area = getCoveredAreaFromFixtureData()

    pd.testing.assert_frame_equal(properties_covered_area_data, expected_covered_area)


def test_validatePropertyTotalArea(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_total_area_data = provider.getDataFromProperties()[
        "total_area"
    ].to_frame()

    expected_total_area = getTotalAreaFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_area_data, expected_total_area)


def test_validatePropertyDescription(fixture_description_data):
    provider = zonapropProvider(
        fixture_description_data, "https://www.zonaprop.com.ar/"
    )
    properties_description_data = provider.getDataFromProperties()[
        "description"
    ].to_frame()

    expected_description = getDescriptionFromFixtureData()

    pd.testing.assert_frame_equal(properties_description_data, expected_description)


def test_validatePropertyParking(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_parking_data = provider.getDataFromProperties()["parking"].to_frame()

    expected_parking = getParkingFromFixtureData()

    pd.testing.assert_frame_equal(properties_parking_data, expected_parking)


def test_validatePropertyCurrency(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_currency_data = provider.getDataFromProperties()["currency"].to_frame()

    expected_currency = getCurrencyFromFixtureData()
    pd.testing.assert_frame_equal(properties_currency_data, expected_currency)


def test_validatePropertyUrl(fixture_description_data):
    provider = zonapropProvider(
        fixture_description_data, "https://www.zonaprop.com.ar/"
    )
    properties_url_data = provider.getDataFromProperties()["url"].to_frame()

    expected_url = getUrlFromFixtureData()
    pd.testing.assert_frame_equal(properties_url_data, expected_url)


def test_validatePropertyLocation(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    properties_location_data = provider.getDataFromProperties()["location"].to_frame()

    expected_location = getLocationFromFixtureData()

    pd.testing.assert_frame_equal(properties_location_data, expected_location)


def test_validateRealStateAgency(fixture_real_state_agency_and_reserved_data):
    provider = zonapropProvider(
        fixture_real_state_agency_and_reserved_data, "https://www.zonaprop.com.ar/"
    )
    properties_real_state_agency_data = provider.getDataFromProperties()[
        "real_state_agency"
    ].to_frame()

    expected_real_state_agency = getRealStateAgencyFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_real_state_agency_data, expected_real_state_agency
    )


def test_validatePropertyReserved(fixture_real_state_agency_and_reserved_data):
    provider = zonapropProvider(
        fixture_real_state_agency_and_reserved_data, "https://www.zonaprop.com.ar/"
    )
    properties_reserved_properties_data = provider.getDataFromProperties()[
        "reserved"
    ].to_frame()

    expected_reserved_properties = getReservedPropertiesFromFixtureData()

    pd.testing.assert_frame_equal(
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
    propertiesTypeData = provider.getDataFromProperties()["provider"].to_frame()

    expectedProvider = getProviderFromFixtureData()

    pd.testing.assert_frame_equal(propertiesTypeData, expectedProvider)


@freeze_time("2000-01-01 12:00:00")
def test_validateDownloadDate(fixture_data):
    provider = zonapropProvider(fixture_data, "https://www.zonaprop.com.ar/")
    propertiesTypeData = provider.getDataFromProperties()["download_date"].to_frame()

    expectedProvider = getDownloadDateFromFixtureData()

    pd.testing.assert_frame_equal(propertiesTypeData, expectedProvider)
