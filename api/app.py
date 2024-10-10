from flask import Flask, jsonify, request, g
from utils import (
    executeQuery,
    filterHandler,
    parseDate,
    getNewPropertyDescriptions,
    fetchFullPropertyDetails,
    getPreviousDate,
    conn,
    handlers,
)

app = Flask(__name__)


@app.route("/locations")
def get_locations():
    """
    Retrieves distinct locations from the property_data table and returns them as a JSON response.
    """
    query = "SELECT DISTINCT location FROM property_data ORDER BY location ASC;"
    locations = [row[0] for row in executeQuery(query)]
    return jsonify({"locations": locations})


@app.route("/properties/filter")
def get_properties_by_filter():
    """
    Filters properties based on the query parameters provided in the request.
    """
    try:
        filters = {key: value for key, value in request.args.items() if key in handlers}
        where_clause = [filterHandler(key, value) for key, value in filters.items()]

        query = f"SELECT * FROM property_data WHERE {' AND '.join(where_clause)};"
        properties = executeQuery(query)

        return jsonify(properties)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400


@app.route("/properties/new/<provided_date>")
def get_new_properties(providedDate):
    """
    This endpoint retrieves properties uploaded on the provided date that were not available the day before.
    """
    try:
        providedDateString = parseDate(providedDate)
    except ValueError:
        return jsonify({"error": "Invalid date filter format: date"}), 400

    try:
        previousDateString = getPreviousDate(providedDate)
        newDescriptions = getNewPropertyDescriptions(
            providedDateString, previousDateString
        )
        newProperties = fetchFullPropertyDetails(newDescriptions)

    except Exception as error:
        return jsonify({"error": f"An error occurred: {error}"}), 500

    return jsonify(newProperties)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
