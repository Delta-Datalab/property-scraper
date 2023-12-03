import os
import numpy as np
import pytest
import pandas as pd

from src.browser import Browser
from src.scraper import Scraper
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
def scraper():
    return Scraper(Browser())


def getPricesFromFixtureData():
    return np.array(
        [
            ["Consultar precio"],
            ["Consultar precio"],
            ["$ 200.000"],
            ["Consultar precio"],
            ["Consultar precio"],
            ["Consultar precio"],
            ["$ 350.000"],
            ["$ 400.000"],
            ["$ 380.000"],
            ["Consultar precio"],
            ["Consultar precio"],
            ["Consultar precio"],
            ["$ 370.000"],
            ["$ 350.000"],
            ["Consultar precio"],
            ["Consultar precio"],
            ["$ 230.000"],
            ["Consultar precio"],
            ["$ 400.000"],
            ["$ 380.000"],
        ]
    )


def getExpensesFromFixtureData():
    return np.array(
        [
            ["$ 65.000 Expensas"],
            ["$ 70.000 Expensas"],
            ["$ 50.000 Expensas"],
            ["$ 120.000 Expensas"],
            ["$ 72.300 Expensas"],
            ["$ 70.000 Expensas"],
            ["$ 18.500 Expensas"],
            ["$ 24.300 Expensas"],
            [np.nan],
            [np.nan],
            ["$ 40.000 Expensas"],
            ["$ 70.000 Expensas"],
            ["$ 22.000 Expensas"],
            ["$ 30.700 Expensas"],
            ["$ 75.000 Expensas"],
            ["$ 62.000 Expensas"],
            ["$ 18.000 Expensas"],
            ["$ 60.000 Expensas"],
            ["$ 34.200 Expensas"],
            ["$ 28.500 Expensas"],
        ]
    )


def getBathroomsFromFixtureData():
    return np.array(
        [
            ["1 baño"],
            ["2 baños"],
            ["1 baño"],
            ["2 baños"],
            ["1 baño"],
            ["2 baños"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            [np.nan],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["1 baño"],
            ["2 baños"],
        ]
    )


def getBedroomsFromFixtureData():
    return np.array(
        [
            ["1 dorm."],
            ["2 dorm."],
            ["2 dorm."],
            ["2 dorm."],
            ["1 dorm."],
            ["2 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            [np.nan],
            [np.nan],
            ["1 dorm."],
            ["3 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["1 dorm."],
            ["2 dorm."],
        ]
    )


def getTotalRoomsFromFixtureData():
    return np.array(
        [
            ["2 amb."],
            ["3 amb."],
            ["3 amb."],
            ["3 amb."],
            ["2 amb."],
            ["3 amb."],
            ["2 amb."],
            ["2 amb."],
            ["1 amb."],
            ["1 amb."],
            ["2 amb."],
            ["4 amb."],
            ["2 amb."],
            ["2 amb."],
            ["2 amb."],
            ["2 amb."],
            ["2 amb."],
            ["2 amb."],
            ["2 amb."],
            [np.nan],
        ]
    )


def getCoveredAreaFromFixtureData():
    return np.array(
        [
            ["50 m²"],
            ["74 m²"],
            ["70 m²"],
            ["73 m²"],
            ["82 m²"],
            ["70 m²"],
            ["48 m²"],
            ["46 m²"],
            ["42 m²"],
            ["35 m²"],
            ["40 m²"],
            ["133 m²"],
            ["40 m²"],
            [np.nan],
            ["53 m²"],
            ["50 m²"],
            ["40 m²"],
            ["48 m²"],
            ["39 m²"],
            ["75 m²"],
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
