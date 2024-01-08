import numpy as np
import pandas as pd


def getPricesFromFixtureData():
    data = [
        "Consultar precio",
        "Consultar precio",
        "$ 200.000",
        "Consultar precio",
        "Consultar precio",
        "Consultar precio",
        "$ 350.000",
        "$ 400.000",
        "$ 380.000",
        "Consultar precio",
        "Consultar precio",
        "Consultar precio",
        "USD 370.000",
        "$ 350.000",
        "Consultar precio",
        "Consultar precio",
        "$ 230.000",
        "Consultar precio",
        "$ 400.000",
        "$ 380.000",
    ]

    pricesDf = pd.Series(data)
    return pricesDf


def getExpensesFromFixtureData():
    data = [
        "$ 65.000 Expensas",
        "$ 70.000 Expensas",
        "$ 50.000 Expensas",
        "$ 120.000 Expensas",
        "$ 72.300 Expensas",
        "$ 70.000 Expensas",
        "$ 18.500 Expensas",
        "$ 24.300 Expensas",
        pd.NA,
        pd.NA,
        "$ 40.000 Expensas",
        "$ 70.000 Expensas",
        "$ 22.000 Expensas",
        "$ 30.700 Expensas",
        "$ 75.000 Expensas",
        "$ 62.000 Expensas",
        "$ 18.000 Expensas",
        "$ 60.000 Expensas",
        "$ 34.200 Expensas",
        "$ 28.500 Expensas",
    ]

    expensesDf = pd.Series(data)
    return expensesDf


def getExpensesCurrencyFromFixtureData():
    data = [
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        pd.NA,
        pd.NA,
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
    ]

    expensesCurrencyDf = pd.Series(data)
    return expensesCurrencyDf


def getBathroomsFromFixtureData():
    data = [
        "1 baño",
        "2 baños",
        "1 baño",
        "2 baños",
        "1 baño",
        "2 baños",
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        pd.NA,
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        "1 baño",
        "2 baños",
    ]

    bathroomsDf = pd.Series(data)
    return bathroomsDf


def getBedroomsFromFixtureData():
    data = [
        "1 dorm.",
        "2 dorm.",
        "2 dorm.",
        "2 dorm.",
        "1 dorm.",
        "2 dorm.",
        "1 dorm.",
        "1 dorm.",
        pd.NA,
        pd.NA,
        "1 dorm.",
        "3 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "2 dorm.",
    ]

    bedroomsDf = pd.Series(data)
    return bedroomsDf


def getTotalRoomsFromFixtureData():
    data = [
        "2 amb.",
        "3 amb.",
        "3 amb.",
        "3 amb.",
        "2 amb.",
        "3 amb.",
        "2 amb.",
        "2 amb.",
        "1 amb.",
        "1 amb.",
        "2 amb.",
        "4 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        pd.NA,
    ]

    totalRoomsDf = pd.Series(data)
    return totalRoomsDf


def getCoveredAreaFromFixtureData():
    data = [
        50,
        74,
        70,
        73,
        82,
        70,
        48,
        46,
        42,
        35,
        40,
        133,
        40,
        pd.NA,
        53,
        50,
        40,
        48,
        39,
        75,
    ]

    coveredAreaDf = pd.Series(data)
    return coveredAreaDf


def getTotalAreaFromFixtureData():
    data = [
        55,
        92,
        70,
        104,
        136,
        110,
        48,
        51,
        42,
        35,
        45,
        133,
        40,
        50,
        64,
        50,
        40,
        55,
        43,
        85,
    ]

    totalAreaDf = pd.Series(data)
    return totalAreaDf


def getCurrencyFromFixtureData():
    data = [
        pd.NA,
        pd.NA,
        "$",
        pd.NA,
        pd.NA,
        pd.NA,
        "$",
        "$",
        "$",
        pd.NA,
        pd.NA,
        pd.NA,
        "USD",
        "$",
        pd.NA,
        pd.NA,
        "$",
        pd.NA,
        "$",
        "$",
    ]

    currencyDf = pd.Series(data)
    return currencyDf


def getDescriptionFromFixtureData():
    data = [
        "Impecable monoambiente ubicado en plena Recoleta, a metros de la plaza Vicente Lopez. Consta de un área principal que abarca living, comedor y la zona de dormir separada elegantemente por una mampara. Baño y cocinas hechas a nuevo. Todos los muebles y el equipamiento son de primera calidad y buen gusto. Muy luminoso, apacible y silencioso. Con seguridad 24 hs. Apto para alquiler temporario a partir de los 3 meses. (No se aceptan mascotas)",
        "Xintel(lor-lor-1693) Alquiler de Departamento monoambiente en Boedo, Capital Federal. 1 ambiente - oficina con vivienda en alquiler - apto vivienda también - se alquila para uso profesional con vivienda - monoambiente con patio - cocina integrada - baño completo - A estrenar - pocos departamentos - excelente ubicación - interno / lateral. - loria inmobiliaria. cpi 1. 300 / 8. 528 caba",
    ]

    descriptionDf = pd.Series(data)
    return descriptionDf


def getParkingFromFixtureData():
    data = [
        "1 coch.",
        "1 coch.",
        pd.NA,
        "1 coch.",
        "1 coch.",
        "2 coch.",
        pd.NA,
        pd.NA,
        "1 coch.",
        pd.NA,
        "1 coch.",
        "1 coch.",
        pd.NA,
        pd.NA,
        "1 coch.",
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
    ]

    parkingDf = pd.Series(data)
    return parkingDf


def getUrlFromFixtureData():
    data = [
        "/propiedades/impecable-monoambiente-ubicado-en-plena-recoleta-52612984.html",
        "/propiedades/1-ambiente-uso-profesional-y-vivienda-estrenar.-52721443.html",
    ]

    urlDf = pd.Series(data)
    return urlDf


def getLocationFromFixtureData():
    data = [
        "Núñez, Capital Federal",
        "Pueblo Caamaño, Pilar",
        "Echesortu, Rosario",
        "Champagnat, Pilar",
        "Bouquet, Pilar",
        "Terrazas de Ayres, Manuel Alberti",
        "Olivos, Vicente López",
        "Almagro, Capital Federal",
        "Vohe, Pilar",
        "Villa Crespo, Capital Federal",
        "Palermo Hollywood, Palermo",
        "La Reserva Cardales, Campana",
        "Palermo Chico, Palermo",
        "Villa Urquiza, Capital Federal",
        "Vicente López, GBA Norte",
        "San Nicolás, Capital Federal",
        "Centro, Córdoba",
        "Puerto Madero, Capital Federal",
        "Núñez, Capital Federal",
        "Martin, Rosario",
    ]

    locationDf = pd.Series(data)
    return locationDf


def getRealStateAgencyFromFixtureData():
    data = [
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ]

    realStateAgencyDf = pd.Series(data)
    return realStateAgencyDf


def getReservedPropertiesFromFixtureData():
    data = [
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]

    reservedPropertiesDf = pd.Series(data)
    return reservedPropertiesDf


def getProviderFromFixtureData():
    data = ["Zonaprop" for _ in range(20)]

    providerDf = pd.Series(data)
    return providerDf


def getDownloadDateFromFixtureData():
    data = ["2000-01-01 12:00:00" for _ in range(20)]

    downloadDateDf = pd.Series(data)
    return downloadDateDf
