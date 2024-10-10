import os
import psycopg2
import urllib.parse
from datetime import timedelta, datetime
import re

# Get database credentials from environment variables
DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "property_db")
DB_USER = os.environ.get("POSTGRES_USER", "root")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "root")

# Connect to the database
conn = psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
)

# Global handler mapping
handlers = {
    "min_price": lambda v: f"price >= {float(v)}",
    "max_price": lambda v: f"price <= {float(v)}",
    "currency": lambda v: f"currency LIKE '%{v}%'",
    "location": lambda v: handleLocation(v),
    "total_rooms": lambda v: f"total_rooms = {int(v)}",
    "min_bedrooms": lambda v: f"bedrooms >= {int(v)}",
    "parking": lambda v: handleParking(v),
    "date": lambda v: f"date = '{parseDate(v)}'",
    "real_state_agency": lambda v: f"real_state_agency = {stringToBool(v)}",
}


def executeQuery(query, params=None):
    """
    Executes a SQL query with optional parameters and returns the results.
    """
    cur = conn.cursor()
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()
    return results


def stringToBool(value):
    """
    Converts a string value to a boolean.
    """
    return value.lower() == "true"


def parseDate(value):
    """
    Parses a date string and formats it for SQL.
    """
    try:
        dateObject = datetime.strptime(value, "%d %b %Y")
        return dateObject.strftime("%a, %d %b %Y %H:%M:%S GMT")
    except ValueError:
        raise ValueError("Invalid date format for filter: date")


def handleLocation(value):
    """
    Parses and handles the location filter.
    """
    try:
        decodedValue = urllib.parse.unquote(value, encoding="utf-8")
        neighborhood = decodedValue.split(",", 1)[0]
        return f"(location LIKE '%{neighborhood}%' OR location = '{value}')"
    except Exception as e:
        raise ValueError(f"Error decoding location: {str(e)}")


def handleParking(value):
    """
    Parses and handles the parking filter.
    """
    if value == "1":
        return "parking = 1"
    else:
        raise ValueError("Invalid value for filter: parking")


def filterHandler(key, value):
    """
    Handles filters for the property data.
    """
    if key not in handlers:
        raise ValueError(f"Invalid filter key: {key}")
    return handlers[key](value)


def getPreviousDate(providedDate):
    """
    Returns the formatted string of the day before the provided date.
    """
    providedDateObject = datetime.strptime(providedDate, "%d %b %Y")
    previousDateObject = providedDateObject - timedelta(days=1)
    return parseDate(previousDateObject.strftime("%d %b %Y"))


def fetchDescriptions(dateString):
    """
    Fetches property descriptions for a given date.
    """
    query = "SELECT description FROM property_data WHERE date = %s"
    return {row[0] for row in executeQuery(query, (dateString,))}


def getNewPropertyDescriptions(providedDateString, previousDateString):
    """
    Returns descriptions of properties that are new on the provided date compared to the previous date.
    """
    providedDateDescriptions = fetchDescriptions(providedDateString)
    previousDateDescriptions = fetchDescriptions(previousDateString)

    return providedDateDescriptions - previousDateDescriptions


def fetchFullPropertyDetails(newDescriptions):
    """
    Fetches the full details of new properties based on the description.
    """
    newProperties = []
    newPropertyQuery = "SELECT * FROM property_data WHERE description = %s"

    for description in newDescriptions:
        newProperty = executeQuery(newPropertyQuery, (description,))
        if newProperty:
            newProperties.append(newProperty[0])

    return newProperties
