import numpy as np
import pandas as pd


def getPricesFromFixtureData():
    data = [
        "Consultar precio",
        "$ 200.000",
        "USD 490",
        "$ 280.000",
        "$ 300.000",
        "$ 350.000",
        "$ 300.000",
        "$ 280.000",
        "$ 400.000",
        "$ 330.000",
        "$ 230.000",
        "$ 300.000",
        "USD 450",
        "USD 400",
        "$ 400.000",
        "$ 270.000",
        "$ 260.000",
        "$ 300.000",
        "$ 300.000",
        "$ 350.000",
    ]

    pricesDf = pd.Series(data)
    return pricesDf


def getExpensesFromFixtureData():
    data = [
        "$ 80.000 Expensas",
        "$ 12.000 Expensas",
        "$ 32.000 Expensas",
        "$ 580.000 Expensas",
        "$ 97.000 Expensas",
        "$ 52.510 Expensas",
        pd.NA,
        "$ 63.000 Expensas",
        "$ 45.000 Expensas",
        pd.NA,
        pd.NA,
        pd.NA,
        "$ 65.000 Expensas",
        pd.NA,
        "$ 28.000 Expensas",
        pd.NA,
        "$ 17.000 Expensas",
        "$ 22.000 Expensas",
        "$ 30.000 Expensas",
        "$ 55.000 Expensas",
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
        pd.NA,
        "$",
        "$",
        pd.NA,
        pd.NA,
        pd.NA,
        "$",
        pd.NA,
        "$",
        pd.NA,
        "$",
        "$",
        "$",
        "$",
    ]

    expensesCurrencyDf = pd.Series(data)
    return expensesCurrencyDf


def getBathroomsFromFixtureData():
    data = [
        pd.NA,
        "1 baño",
        "1 baño",
        "1 baño",
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
        "2 baños",
        "2 baños",
        "1 baño",
        "1 baño",
        "2 baños",
        "1 baño",
    ]

    bathroomsDf = pd.Series(data)
    return bathroomsDf


def getBedroomsFromFixtureData():
    data = [
        pd.NA,
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        "1 dorm.",
        pd.NA,
        "2 dorm.",
        "2 dorm.",
        "1 dorm.",
        "1 dorm.",
        "2 dorm.",
        "1 dorm.",
    ]

    bedroomsDf = pd.Series(data)
    return bedroomsDf


def getTotalRoomsFromFixtureData():
    data = [
        pd.NA,
        pd.NA,
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "2 amb.",
        "1 amb.",
        "4 amb.",
        "4 amb.",
        "3 amb.",
        "2 amb.",
        "5 amb.",
        "1 amb.",
    ]

    totalRoomsDf = pd.Series(data)
    return totalRoomsDf


def getCoveredAreaFromFixtureData():
    data = [
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
    ]

    coveredAreaDf = pd.Series(data)
    return coveredAreaDf


def getTotalAreaFromFixtureData():
    data = [
        52,
        45,
        40,
        65,
        45,
        46,
        45,
        44,
        47,
        45,
        40,
        100,
        63,
        39,
        75,
        94,
        40,
        41,
        90,
        35,
    ]

    totalAreaDf = pd.Series(data)
    return totalAreaDf


def getCurrencyFromFixtureData():
    data = [
        pd.NA,
        "$",
        "USD",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
        "USD",
        "USD",
        "$",
        "$",
        "$",
        "$",
        "$",
        "$",
    ]

    currencyDf = pd.Series(data)
    return currencyDf


def getDescriptionFromFixtureData():
    data = [
        "Excelente monoambiente en alquiler disponible a partir del 23 de Enero de 2023, en edificio Torre Plaza en calle Rivadavia 1750 con entrada también por el Pasaje que está en la Plaza. Muy luminoso. Calefacción por losa radiante con controles individuales de temperatura. Amplio ambiente único con placard y acceso a balcón con lindísimas vistas hacia zona Grand Bourg. Baño completo con bañadera. Termotanque y lugar para instalar lavarropas oculto por un placard. Cocina independiente equipada. Actualización cuatrimestral por índice ipc que publica el indec. Expensas aproximadas $ 20. 000 x mes. Contrato por dos años. Locatario y colocatario deben presentar o recibos de sueldos (si tienen relación de dependiencia) o certificacion de facturacion año 2022 y 2023 más form F713 de ganancias de la Afip (año 2022 - sin son responsables inscriptos) o seguro de caución a satisfacción del propietario. Al momento de la firma del contrato se debe abonar un mes de alquiler adelantado, un mes de depósito de garantía, el 4, 15% del monto total del contrato como honorarios profesionales regulados por el colegio (en el caso de un contrato x 22 años equivale a un mes del alquiler), más las certificaciones de firma del locatario y su garante ante escribano público (hoy $ 8. 000 cada firma). Ambientes: Ambiente principal (si) Baño. Lavadero cubierto (si) Quincho con parrilla. Salón usos múltiples. Servicios: Electricidad, Pavimento, Cloacas, Gas, Teléfono, Agua Corriente, Videocable. Otros Servicios: Terraza, Balcón. Las superficies y medidas son estimadas y surgen de información proporcionada por el propietario, las reales surgiran de lo registrado en la cédula parcelaria. Operación supeditada a que el propietario cumpla con la Reg. 2371, coti con la afip. Quedo a vuestra disposición para evacuar cualquier duda o consulta. Juan M. Figueroa Villegas. Martillero y Corredor Público Nacional. Corredor Inmobiliario - M. P. Nº 99. Martín Cornejo 290 - Salta. Cel: Ver datos - Fijo: Ver datos. ar",
        "Domus Bienes Raíces Alquila Departamento en Macrocentro. El departamento se distribuye de la siguiente manera: 1 dormitorio. Baño completo. Cocina. Living. Cochera. Cuenta con calefacción central. Contrafrente. El precio es dólares billete, primer año de contrato sin incrementos y el segundo año con un incremento de 10%. Contrato por 2 años. G. R. contáctenos hoy mismo para mayor información. Corredor Inmobiliario: Gonzalo Rubio - cucis 452. Corredor Inmobiliario: Gonzalo Paris- cucis 441. domus bienes raices. Leguizamón 979, Planta Baja, Oficina B",
        "Departamento en ph de dos ambientes en planta baja sobre av. Presidente peron entre irigoin Y pringles. Living comedor con cocina incorporada, sin artefacto de cocina. Dormitorio con placard. Baño completo. Ventanas con mosquitero Y persiana. Maximo 2 personas. No se aceptan mascotas. Las expensas incluyen la tasa municipal Y servicio de aysa. Sin cochera. Consultanos por whatsapp! Aviso publicado por Pixel Inmobiliario (Servicio de Páginas Web para Inmobiliarias). #1250",
        "Dpto, con dormitorio en planta alta, con placard y baño. En planta baja, cocina comedor, sin aparato de cocina.",
    ]

    descriptionDf = pd.Series(data)
    return descriptionDf


def getParkingFromFixtureData():
    data = [
        pd.NA,
        pd.NA,
        pd.NA,
        "1 coch.",
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        "1 coch.",
        pd.NA,
        pd.NA,
        pd.NA,
        pd.NA,
        "1 coch.",
        pd.NA,
        pd.NA,
        pd.NA,
        "1 coch.",
        "1 coch.",
        pd.NA,
    ]

    parkingDf = pd.Series(data)
    return parkingDf


def getUrlFromFixtureData():
    data = [
        "/propiedades/clasificado/alclapin-exc.-monoambiente-alq.-en-rivadavia-1750-48425571.html",
        "/propiedades/clasificado/alclapin-alquiler-departamento-un-dormitorio-53057853.html",
        "/propiedades/clasificado/alclapin-departamento-2-ambientes-en-planta-baja-sin-patio.-52806868.html",
        "/propiedades/clasificado/alclapin-talcahuano-700-52888466.html",
    ]

    urlDf = pd.Series(data)
    return urlDf


def getLocationFromFixtureData():
    data = [
        "Recoleta, Capital Federal",
        "General Pueyrredón, Córdoba",
        "Belgrano R, Belgrano",
        "General Paz, Córdoba",
        "Belgrano, Capital Federal",
        "Almagro, Capital Federal",
        "Rosario, Santa Fe",
        "Alto Alberdi, Córdoba",
        "General Paz, Córdoba",
        "Nueva Córdoba, Córdoba",
        "Pichincha, Rosario",
        "Distrito Centro, Rosario",
        "Barrancas, Capital Federal",
        "Bahía Grande, Nordelta",
        "General Paz, Córdoba",
        "General José de San Martín, Distrito Sur",
        "Paso de los Andes, Córdoba",
        "Castelar, Morón",
        "Villa Carlos Paz, Córdoba",
        "Belgrano, Capital Federal",
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
