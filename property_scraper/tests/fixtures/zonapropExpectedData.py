import numpy as np


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
