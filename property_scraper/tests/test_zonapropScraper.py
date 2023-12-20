import os
import numpy as np
import pytest
import pandas as pd

from src.browser import Browser
from src.scraper import Scraper
from src.provieder import *
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
        os.getcwd(),
        "tests",
        "fixtures",
        "zonapropFixture_realStateAgencyAndReserved.html",
    )
    with open(fixture_directory, "r") as file:
        html_content = file.read()
    return BeautifulSoup(html_content, "html.parser")


@pytest.fixture
def scraper():
    return Scraper(Browser())


def test_validatePropertyPrices(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_prices_data = provieder.getDataFromProperties()["price"].to_frame()

    expected_prices = getPricesFromFixtureData()
    
    properties = provieder.getDataFromProperties().to_csv("prueba.csv")

    pd.testing.assert_frame_equal(properties_prices_data, expected_prices)


def test_validatePropertyExpenses(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_expenses_data = provieder.getDataFromProperties()["expenses"].to_frame()

    expected_expenses = getExpensesFromFixtureData()

    pd.testing.assert_frame_equal(properties_expenses_data, expected_expenses)


def test_validatePropertyExpensesType(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_expenses_type_data = provieder.getDataFromProperties()[
        "expenses_type"
    ].to_frame()

    expected_expenses_type = getExpensesTypeFromFixtureData()

    pd.testing.assert_frame_equal(properties_expenses_type_data, expected_expenses_type)


def test_validatePropertyBathrooms(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_bathroom_data = provieder.getDataFromProperties()["bathrooms"].to_frame()

    expected_bathrooms = getBathroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bathroom_data, expected_bathrooms)


def test_validatePropertyBedrooms(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_bedrooms_data = provieder.getDataFromProperties()["bedrooms"].to_frame()

    expected_bedrooms = getBedroomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_bedrooms_data, expected_bedrooms)


def test_validatePropertyTotalRooms(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_total_rooms_data = provieder.getDataFromProperties()[
        "total_rooms"
    ].to_frame()

    expected_total_rooms = getTotalRoomsFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_rooms_data, expected_total_rooms)


def test_validatePropertyCoveredArea(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_covered_area_data = provieder.getDataFromProperties()[
        "covered_area"
    ].to_frame()

    expected_covered_area = getCoveredAreaFromFixtureData()

    print(properties_covered_area_data)
    print(expected_covered_area)

    pd.testing.assert_frame_equal(properties_covered_area_data, expected_covered_area)


def test_validatePropertyTotalArea(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_total_area_data = provieder.getDataFromProperties()[
        "total_area"
    ].to_frame()

    expected_total_area = getTotalAreaFromFixtureData()

    pd.testing.assert_frame_equal(properties_total_area_data, expected_total_area)


def test_validatePropertyDescription(fixture_description_data):
    provieder = Provieder(fixture_description_data, zonapropProvieder())
    properties_description_data = provieder.getDataFromProperties()[
        "description"
    ].to_frame()

    expected_description = getDescriptionFromFixtureData()

    pd.testing.assert_frame_equal(properties_description_data, expected_description)


def test_validatePropertyParking(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_parking_data = provieder.getDataFromProperties()["parking"].to_frame()

    expected_parking = getParkingFromFixtureData()

    pd.testing.assert_frame_equal(properties_parking_data, expected_parking)


def test_validatePropertyCurrency(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_currency_data = provieder.getDataFromProperties()["currency"].to_frame()

    expected_currency = getCurrencyFromFixtureData()
    pd.testing.assert_frame_equal(properties_currency_data, expected_currency)


def test_validatePropertyUrl(fixture_description_data):
    provieder = Provieder(fixture_description_data, zonapropProvieder())
    properties_url_data = provieder.getDataFromProperties()["url"].to_frame()

    expected_url = getUrlFromFixtureData()
    pd.testing.assert_frame_equal(properties_url_data, expected_url)


def test_validatePropertyLocation(fixture_data):
    provieder = Provieder(fixture_data, zonapropProvieder())
    properties_location_data = provieder.getDataFromProperties()["location"].to_frame()

    expected_location = getLocationFromFixtureData()

    pd.testing.assert_frame_equal(properties_location_data, expected_location)


def test_validateRealStateAgency(fixture_real_state_agency_and_reserved_data):
    provieder = Provieder(
        fixture_real_state_agency_and_reserved_data, zonapropProvieder()
    )
    properties_real_state_agency_data = provieder.getDataFromProperties()[
        "real_state_agency"
    ].to_frame()

    expected_real_state_agency = getRealStateAgencyFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_real_state_agency_data, expected_real_state_agency
    )


def test_validatePropertyReserved(fixture_real_state_agency_and_reserved_data):
    provieder = Provieder(
        fixture_real_state_agency_and_reserved_data, zonapropProvieder()
    )
    properties_reserved_properties_data = provieder.getDataFromProperties()[
        "reserved"
    ].to_frame()

    expected_reserved_properties = getReservedPropertiesFromFixtureData()

    pd.testing.assert_frame_equal(
        properties_reserved_properties_data, expected_reserved_properties
    )
