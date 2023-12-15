import os
import numpy as np
import pytest
import pandas as pd

from src.browser import Browser
from src.scraper import Scraper
from tests.fixtures.zonapropExpectedData import *
from bs4 import BeautifulSoup


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
        os.getcwd(), "tests", "fixtures", "zonapropFixture_realStateAgent.html"
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


@pytest.fixture
def scraper():
    return Scraper(Browser())


def test_validatePropertyPrices(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_prices_data = scraper.getPricesFromProperties(properties)

    expected_prices = getPricesFromFixtureData()

    pd.testing.assert_frame_equal(properties_prices_data, expected_prices)


def test_validatePropertyExpenses(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_prices_data = scraper.getExpensesFromProperties(properties)

    expected_expenses = getExpensesFromFixtureData()

    pd.testing.assert_frame_equal(properties_prices_data, expected_expenses)


def test_validatePropertyExpensesType(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_expenses_type_data = scraper.getExpensesTypeFromProperties(properties)

    expected_expenses_type = getExpensesTypeFromFixtureData()

    pd.testing.assert_frame_equal(properties_expenses_type_data, expected_expenses_type)


def test_validatePropertyBathrooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_bathroom_data = scraper.getBathroomsFromProperties(properties)

    expected_bathrooms = getBathroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bathroom_data, expected_bathrooms)


def test_validatePropertyBedrooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_bedrooms_data = scraper.getBedroomsFromProperties(properties)

    expected_bedrooms = getBedroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bedrooms_data, expected_bedrooms)


def test_validatePropertyTotalRooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_total_rooms_data = scraper.getTotalRoomsFromProperties(properties)

    expected_total_rooms = getTotalRoomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_rooms_data, expected_total_rooms)


def test_validatePropertyCoveredArea(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_covered_area_data = scraper.getCoveredAreaFromProperties(properties)

    expected_covered_area = getCoveredAreaFromFixtureData()

    print(properties_covered_area_data)
    print(expected_covered_area)

    pd.testing.assert_frame_equal(properties_covered_area_data, expected_covered_area)


def test_validatePropertyTotalArea(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_total_area_data = scraper.getTotalAreaFromProperties(properties)

    expected_total_area = getTotalAreaFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_area_data, expected_total_area)


def test_validatePropertyDescription(fixture_description_data, scraper):
    properties = scraper.getProperties(fixture_description_data, "www.zonaprop.com.ar")
    properties_description_data = scraper.getDescriptionFromProperties(properties)

    expected_description = getDescriptionFromFixtureData()

    pd.testing.assert_frame_equal(properties_description_data, expected_description)


def test_validatePropertyParking(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_parking_data = scraper.getParkingFromProperties(properties)

    expected_parking = getParkingFromFixtureData()

    pd.testing.assert_frame_equal(properties_parking_data, expected_parking)


def test_validatePropertyCurrency(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_currency_data = scraper.getCurrencyFromProperties(properties)

    expected_currency = getCurrencyFromFixtureData()
    pd.testing.assert_frame_equal(properties_currency_data, expected_currency)


def test_validatePropertyUrl(fixture_description_data, scraper):
    properties = scraper.getProperties(fixture_description_data, "www.zonaprop.com.ar")
    properties_url_data = scraper.getUrlFromProperties(properties)

    expected_url = getUrlFromFixtureData()
    pd.testing.assert_frame_equal(properties_url_data, expected_url)


def test_validatePropertyLocation(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_location_data = scraper.getLocationFromProperties(properties)

    expected_location = getLocationFromFixtureData()

    pd.testing.assert_frame_equal(properties_location_data, expected_location)


def test_validateRealStateAgency(fixture_real_state_agency_and_reserved_data, scraper):
    properties = scraper.getProperties(
        fixture_real_state_agency_and_reserved_data, "www.zonaprop.com.ar"
    )
    properties_real_state_agency_data = scraper.getRealStateAgencyFromProperties(
        properties
    )

    expected_real_state_agency = getRealStateAgencyFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_real_state_agency_data, expected_real_state_agency
    )


def test_validatePropertyReserved(fixture_real_state_agency_and_reserved_data, scraper):
    properties = scraper.getProperties(
        fixture_real_state_agency_and_reserved_data, "www.zonaprop.com.ar"
    )
    properties_reserved_properties_data = scraper.getReservedFromProperties(properties)

    expected_reserved_properties = getReservedPropertiesFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_reserved_properties_data, expected_reserved_properties
    )
