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
def scraper():
    return Scraper(Browser())


def getParkingFromFixtureData():
    return np.array(
        [
            ["1 coch."],
            ["1 coch."],
            [np.nan],
            ["1 coch."],
            ["1 coch."],
            ["2 coch."],
            [np.nan],
            [np.nan],
            ["1 coch."],
            [np.nan],
            ["1 coch."],
            ["1 coch."],
            [np.nan],
            [np.nan],
            ["1 coch."],
            [np.nan],
            [np.nan],
            [np.nan],
            [np.nan],
            [np.nan],
        ]
    )


def getUrlFromFixtureData():
    return np.array(
        [
            [
                "/propiedades/impecable-monoambiente-ubicado-en-plena-recoleta-52612984.html"
            ],
            [
                "/propiedades/1-ambiente-uso-profesional-y-vivienda-estrenar.-52721443.html"
            ],
        ]
    )


def getLocationFromFixtureData():
    return np.array(
        [
            ["Núñez, Capital Federal"],
            ["Pueblo Caamaño, Pilar"],
            ["Echesortu, Rosario"],
            ["Champagnat, Pilar"],
            ["Bouquet, Pilar"],
            ["Terrazas de Ayres, Manuel Alberti"],
            ["Olivos, Vicente López"],
            ["Almagro, Capital Federal"],
            ["Vohe, Pilar"],
            ["Villa Crespo, Capital Federal"],
            ["Palermo Hollywood, Palermo"],
            ["La Reserva Cardales, Campana"],
            ["Palermo Chico, Palermo"],
            ["Villa Urquiza, Capital Federal"],
            ["Vicente López, GBA Norte"],
            ["San Nicolás, Capital Federal"],
            ["Centro, Córdoba"],
            ["Puerto Madero, Capital Federal"],
            ["Núñez, Capital Federal"],
            ["Martin, Rosario"],
        ]
    )


def test_validatePropertyPrices(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_prices_data = scraper.getPricesFromProperties(properties).values

    expected_prices = getPricesFromFixtureData()

    assert np.array_equal(properties_prices_data, expected_prices)


def test_validatePropertyExpenses(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_prices_data = scraper.getExpensesFromProperties(properties).values

    expected_expenses = getExpensesFromFixtureData()

    assert np.array_equal(properties_prices_data, expected_expenses)


def test_validatePropertyExpensesType(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_expenses_type_data = scraper.getExpensesTypeFromProperties(
        properties
    ).values

    expected_expenses_type = getExpensesTypeFromFixtureData()

    assert np.array_equal(properties_expenses_type_data, expected_expenses_type)


def test_validatePropertyBathrooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_bathroom_data = scraper.getBathroomsFromProperties(properties).values

    expected_bathrooms = getBathroomsFromFixtureData()

    assert np.array_equal(properties_bathroom_data, expected_bathrooms)


def test_validatePropertyBedrooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_bedrooms_data = scraper.getBedroomsFromProperties(properties).values

    expected_bedrooms = getBedroomsFromFixtureData()

    assert np.array_equal(properties_bedrooms_data, expected_bedrooms)


def test_validatePropertyTotalRooms(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_total_rooms_data = scraper.getTotalRoomsFromProperties(properties).values

    expected_total_rooms = getTotalRoomsFromFixtureData()

    assert np.array_equal(properties_total_rooms_data, expected_total_rooms)


def test_validatePropertyCoveredArea(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_covered_area_data = scraper.getCoveredAreaFromProperties(
        properties
    ).values

    expected_covered_area = getCoveredAreaFromFixtureData()

    assert np.array_equal(properties_covered_area_data, expected_covered_area)


def test_validatePropertyTotalArea(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_total_area_data = scraper.getTotalAreaFromProperties(properties).values

    expected_total_area = getTotalAreaFromFixtureData()

    assert np.array_equal(properties_total_area_data, expected_total_area)


def test_validatePropertyDescription(fixture_description_data, scraper):
    properties = scraper.getProperties(fixture_description_data, "www.zonaprop.com.ar")
    properties_description_data = scraper.getDescriptionFromProperties(
        properties
    ).values

    expected_description = getDescriptionFromFixtureData()

    assert np.array_equal(properties_description_data, expected_description)


def test_validatePropertyParking(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_parking_data = scraper.getParkingFromProperties(properties).values

    expected_parking = getParkingFromFixtureData()

    assert np.array_equal(properties_parking_data, expected_parking)


def test_validatePropertyCurrency(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_currency_data = scraper.getCurrencyFromProperties(properties).values

    expected_currency = getCurrencyFromFixtureData()
    assert np.array_equal(properties_currency_data, expected_currency)


def test_validatePropertyUrl(fixture_description_data, scraper):
    properties = scraper.getProperties(fixture_description_data, "www.zonaprop.com.ar")
    properties_url_data = scraper.getUrlFromProperties(properties).values

    expected_url = getUrlFromFixtureData()
    assert np.array_equal(properties_url_data, expected_url)


def test_validatePropertyLocation(fixture_data, scraper):
    properties = scraper.getProperties(fixture_data, "www.zonaprop.com.ar")
    properties_location_data = scraper.getLocationFromProperties(properties).values

    expected_location = getLocationFromFixtureData()

    assert np.array_equal(properties_location_data, expected_location)
