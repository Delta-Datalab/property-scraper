from flask import Flask, jsonify, request, g
from utils import executeQuery, filterHandler, conn, handlers

app = Flask(__name__)

@app.route('/locations')
def get_locations():
    """
    Retrieves distinct locations from the property_data table and returns them as a JSON response.
    """
    query = "SELECT DISTINCT location FROM property_data ORDER BY location ASC;"
    locations = [row[0] for row in executeQuery(query)]
    return jsonify({'locations': locations})

# curl http://localhost:5000/properties/filter?min_price=150000&max_price=250000&min_bedrooms=2&date=01%20Jan%202024
@app.route('/properties/filter')
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
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)