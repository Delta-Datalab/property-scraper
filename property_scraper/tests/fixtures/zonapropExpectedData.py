import numpy as np
import pandas as pd


def getPricesFromFixtureData():
    data = [
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

    prices_df = pd.DataFrame(data, columns=["price"])
    return prices_df


def getExpensesFromFixtureData():
    data = [
        ["$ 65.000 Expensas"],
        ["$ 70.000 Expensas"],
        ["$ 50.000 Expensas"],
        ["$ 120.000 Expensas"],
        ["$ 72.300 Expensas"],
        ["$ 70.000 Expensas"],
        ["$ 18.500 Expensas"],
        ["$ 24.300 Expensas"],
        [pd.NA],
        [pd.NA],
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

    expenses_df = pd.DataFrame(data, columns=["expenses"])
    return expenses_df


def getExpensesCurrencyFromFixtureData():
    data = [
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        [pd.NA],
        [pd.NA],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
        ["$"],
    ]

    expenses_currency_df = pd.DataFrame(data, columns=["expenses_currency"])
    return expenses_currency_df


def getBathroomsFromFixtureData():
    data = [
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
        [pd.NA],
        ["1 baño"],
        ["1 baño"],
        ["1 baño"],
        ["1 baño"],
        ["1 baño"],
        ["1 baño"],
        ["1 baño"],
        ["2 baños"],
    ]

    bathrooms_df = pd.DataFrame(data, columns=["bathrooms"])
    return bathrooms_df


def getBedroomsFromFixtureData():
    data = [
        ["1 dorm."],
        ["2 dorm."],
        ["2 dorm."],
        ["2 dorm."],
        ["1 dorm."],
        ["2 dorm."],
        ["1 dorm."],
        ["1 dorm."],
        [pd.NA],
        [pd.NA],
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

    bedrooms_df = pd.DataFrame(data, columns=["bedrooms"])
    return bedrooms_df


def getTotalRoomsFromFixtureData():
    data = [
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
        [pd.NA],
    ]

    total_roms_df = pd.DataFrame(data, columns=["total_rooms"])
    return total_roms_df


def getCoveredAreaFromFixtureData():
    data = [
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
        [pd.NA],
        [53],
        [50],
        [40],
        [48],
        [39],
        [75],
    ]

    covered_area_df = pd.DataFrame(data, columns=["covered_area"])
    return covered_area_df


def getTotalAreaFromFixtureData():
    data = [
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

    total_area_df = pd.DataFrame(data, columns=["total_area"])
    return total_area_df


def getCurrencyFromFixtureData():
    data = [
        [pd.NA],
        [pd.NA],
        ["$"],
        [pd.NA],
        [pd.NA],
        [pd.NA],
        ["$"],
        ["$"],
        ["$"],
        [pd.NA],
        [pd.NA],
        [pd.NA],
        ["USD"],
        ["$"],
        [pd.NA],
        [pd.NA],
        ["$"],
        [pd.NA],
        ["$"],
        ["$"],
    ]

    currency_df = pd.DataFrame(data, columns=["currency"])
    return currency_df


def getDescriptionFromFixtureData():
    data = [
        [
            "Impecable monoambiente ubicado en plena Recoleta, a metros de la plaza Vicente Lopez. Consta de un área principal que abarca living, comedor y la zona de dormir separada elegantemente por una mampara. Baño y cocinas hechas a nuevo. Todos los muebles y el equipamiento son de primera calidad y buen gusto. Muy luminoso, apacible y silencioso. Con seguridad 24 hs. Apto para alquiler temporario a partir de los 3 meses. (No se aceptan mascotas)"
        ],
        [
            "Xintel(lor-lor-1693) Alquiler de Departamento monoambiente en Boedo, Capital Federal. 1 ambiente - oficina con vivienda en alquiler - apto vivienda también - se alquila para uso profesional con vivienda - monoambiente con patio - cocina integrada - baño completo - A estrenar - pocos departamentos - excelente ubicación - interno / lateral. - loria inmobiliaria. cpi 1. 300 / 8. 528 caba"
        ],
    ]

    description_df = pd.DataFrame(data, columns=["description"])
    return description_df


def getParkingFromFixtureData():
    data = [
        ["1 coch."],
        ["1 coch."],
        [pd.NA],
        ["1 coch."],
        ["1 coch."],
        ["2 coch."],
        [pd.NA],
        [pd.NA],
        ["1 coch."],
        [pd.NA],
        ["1 coch."],
        ["1 coch."],
        [pd.NA],
        [pd.NA],
        ["1 coch."],
        [pd.NA],
        [pd.NA],
        [pd.NA],
        [pd.NA],
        [pd.NA],
    ]

    parking_df = pd.DataFrame(data, columns=["parking"])
    return parking_df


def getUrlFromFixtureData():
    data = [
        ["/propiedades/impecable-monoambiente-ubicado-en-plena-recoleta-52612984.html"],
        ["/propiedades/1-ambiente-uso-profesional-y-vivienda-estrenar.-52721443.html"],
    ]

    url_df = pd.DataFrame(data, columns=["url"])
    return url_df


def getLocationFromFixtureData():
    data = [
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

    location_df = pd.DataFrame(data, columns=["location"])
    return location_df


def getRealStateAgencyFromFixtureData():
    data = [
        [True],
        [True],
        [True],
        [True],
        [True],
        [False],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
        [True],
    ]

    real_state_agency_df = pd.DataFrame(data, columns=["real_state_agency"])
    return real_state_agency_df


def getReservedPropertiesFromFixtureData():
    data = [
        [True],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
        [False],
    ]

    real_state_agency_df = pd.DataFrame(data, columns=["reserved"])
    return real_state_agency_df
