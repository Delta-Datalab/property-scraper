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
            ["USD 370.000"],
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
            [50],
            [74],
            [70],
            [73],
            [82],
            [70],
            [48],
            [46],
            [42],
            [35],
            [40],
            [133],
            [40],
            ["nan"],
            [53],
            [50],
            [40],
            [48],
            [39],
            [75],
        ],
        dtype=object,
    )


def getTotalAreaFromFixtureData():
    return np.array(
        [
            [55],
            [92],
            [70],
            [104],
            [136],
            [110],
            [48],
            [51],
            [42],
            [35],
            [45],
            [133],
            [40],
            [50],
            [64],
            [50],
            [40],
            [55],
            [43],
            [85],
        ]
    )


def getCurrencyFromFixtureData():
    return np.array(
        [
            [np.nan],
            [np.nan],
            ["$"],
            [np.nan],
            [np.nan],
            [np.nan],
            ["$"],
            ["$"],
            ["$"],
            [np.nan],
            [np.nan],
            [np.nan],
            ["USD"],
            ["$"],
            [np.nan],
            [np.nan],
            ["$"],
            [np.nan],
            ["$"],
            ["$"],
        ]
    )


def getDescriptionFromFixtureData():
    return np.array(
        [
            [
                "Impecable monoambiente ubicado en plena Recoleta, a metros de la plaza Vicente Lopez. Consta de un área principal que abarca living, comedor y la zona de dormir separada elegantemente por una mampara. Baño y cocinas hechas a nuevo. Todos los muebles y el equipamiento son de primera calidad y buen gusto. Muy luminoso, apacible y silencioso. Con seguridad 24 hs. Apto para alquiler temporario a partir de los 3 meses. (No se aceptan mascotas)"
            ],
            [
                "Xintel(lor-lor-1693) Alquiler de Departamento monoambiente en Boedo, Capital Federal. 1 ambiente - oficina con vivienda en alquiler - apto vivienda también - se alquila para uso profesional con vivienda - monoambiente con patio - cocina integrada - baño completo - A estrenar - pocos departamentos - excelente ubicación - interno / lateral. - loria inmobiliaria. cpi 1. 300 / 8. 528 caba"
            ],
        ]
    )


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
