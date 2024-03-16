import os
from flask import Flask, jsonify, request, g
from datetime import timedelta, datetime
import psycopg2  # Import the psycopg2 library for PostgreSQL
import urllib.parse  # Import the urllib.parse library for URL parsing
import re

app = Flask(__name__)

# Get database credentials from environment variables (recommended for security)
DB_HOST = os.environ.get("DB_HOST", "db")  # Use "db" as the default host if not set
DB_NAME = os.environ.get("POSTGRES_DB", "property_db")
DB_USER = os.environ.get("POSTGRES_USER", "root")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "root")

# Connect to the database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

@app.route('/locations')
def get_locations():
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT location FROM property_data ORDER BY location ASC;")
    locations = [row[0] for row in cur.fetchall()]  # Extract location values
    cur.close()
    return jsonify({'locations': locations})

# curl http://localhost:5000/properties/price_range?min_price=100000&max_price=200000
@app.route('/properties/price_range')
def get_properties_by_price_range():
    min_price = float(request.args.get('min_price', 0))
    max_price = float(request.args.get('max_price', float('inf')))

    cur = conn.cursor()
    cur.execute("SELECT * FROM property_data WHERE price BETWEEN %s AND %s;", (min_price, max_price))
    properties = cur.fetchall()
    cur.close()

    return jsonify(properties)

#curl http://localhost:5000/properties/location/Puerto%20Retiro,%20Retiro
@app.route('/properties/location/<location>')
def get_properties_by_location(location):
    cur = conn.cursor()
    cur.execute("SELECT * FROM property_data WHERE location = %s;", (location,))
    properties = cur.fetchall()
    cur.close()

    return jsonify(properties)


@app.route('/properties/new/<provided_date>')
def get_new_properties(provided_date):
    try:
    # Parse the provided date string using the format string
        provided_date_obj = datetime.strptime(provided_date, '%d %b %Y')
    except ValueError:
        return jsonify({'error': 'Invalid date filter format: date'}), 400

    try:
        with conn.cursor() as cur:
            # Get yesterday's date object
            previous_date_obj = provided_date_obj - timedelta(days=1)

            # Extract date part from previous_date_obj for database query
            date_pattern = r'\d{4}-\d{2}-\d{2}'
            database_date_match = re.search(date_pattern, str(previous_date_obj))
            if not database_date_match:
                return jsonify({'error': 'Error extracting date from previous date object'}), 500
            previous_date_str = database_date_match.group()

            # Execute queries and handle potential empty results
            date_query = "SELECT description FROM property_data WHERE date = %s"
            previous_date_query = "SELECT description FROM property_data WHERE date = %s"

            date_descriptions = set()
            cur.execute(date_query, (provided_date_obj,))
            if cur.rowcount > 0:
                date_descriptions = set(row[0] for row in cur.fetchall())

            previous_date_descriptions = set()
            cur.execute(previous_date_query, (previous_date_str,))
            if cur.rowcount > 0:
                previous_date_descriptions = set(row[0] for row in cur.fetchall())

            # Find new properties (descriptions present today but not yesterday)
            new_properties = []
            if previous_date_descriptions:  # Check if there are descriptions from yesterday
                for description in date_descriptions:
                    if description not in previous_date_descriptions:
                        try:  # Handle potential errors in fetching new property details
                            new_property_query = "SELECT * FROM property_data WHERE description = %s"
                            new_property = cur.execute(new_property_query, (description,)).fetchone()
                            if new_property:  # Only append if new_property is not None
                                new_properties.append(new_property)
                            else:
                            # Handle case where description exists but details are missing
                                print(f"Description '{description}' found today but details not available")  # Or log this message
                        except (psycopg2.Error, Exception) as error:
                            return jsonify({'error': f'Error fetching property details: {error}'}), 500

    except Exception as error:
    # Handle any database connection or query execution errors
        return jsonify({'error': f'An error occurred: {error}'}), 500

    return jsonify(new_properties)


# curl http://localhost:5000/properties/filter?min_price=150000&max_price=250000&min_bedrooms=2&date=01%20Jan%202024
@app.route('/properties/filter')
def get_properties_by_filter():
    filters = {}  # Initialize an empty dictionary for filters
    for key, value in request.args.items():
        if key in ('min_price', 'max_price', 'currency', 'total_rooms', 'min_bedrooms', 'location', 'parking', 'date', 'real_state_agency'):
            try:
                if key == 'date':
                # Parse user-provided date (assuming day-month-year format)
                    try:
                        date_obj = datetime.strptime(value, '%d %b %Y')
                        value = date_obj.strftime('%a, %d %b %Y %H:%M:%S GMT')
                    except ValueError:
                        return jsonify({'error': 'Invalid date format for filter: date'}), 400
                else:
                    value = float(value) if key in ('min_price', 'max_price', 'total_rooms', 'min_bedrooms') else str(value)
                filters[key] = value
            except ValueError:
                return jsonify({'error': 'Invalid value for filter: {}'.format(key)}), 400

    # Build the SQL query dynamically based on provided filters
    where_clause = []
    for key, value in filters.items():
        if key in ('min_price', 'max_price'):
            # Handle price filtering using the 'price' column
            comparison = '>=' if key == 'min_price' else '<='
            where_clause.append(f"price {comparison} {value}")

        elif key == 'currency':
            where_clause.append(f"currency LIKE '%{value}%'")  # Match any currency containing the provided value

        elif key == 'location':
            try:
                decoded_value = urllib.parse.unquote(value, encoding='utf-8')
            except Exception as e:
                return jsonify({'error': f'Error decoding location: {str(e)}'}), 400
            try:
                neighborhood = decoded_value.split(',', 1)[0]
            except ValueError:  # Handle cases without a comma
                return jsonify({'error': 'Invalid location format: Please use "neighborhood, city"'}), 400
            # Build the WHERE clause with LIKE operator (assuming case-insensitive search)
            where_clause.append(f"(location LIKE '%{neighborhood}%' OR location = '{value}')")  # Match full location or neighborhood
        
        elif key == 'total_rooms':
            where_clause.append(f"total_rooms = {value}")

        elif key == 'min_bedrooms':
            where_clause.append(f"bedrooms >= {value}")

        elif key == 'parking':
            try:
                value = True if value.lower() == 'true' else False
            except ValueError:
                return jsonify({'error': 'Invalid value for filter: parking'}), 400
            if value:
                where_clause.append("parking IS NOT NULL AND parking = 1") 
            else:
                where_clause.append("parking IS NULL OR parking = 0")

        elif key == 'date':
            where_clause.append(f"date = '{value}'")
        
        elif key == 'real_state_agency':
            try:
                value = True if value.lower() == 'true' else False
            except ValueError:
                return jsonify({'error': 'Invalid value for filter: real_state_agency'}), 400
            where_clause.append(f"real_state_agency = {value}")

        else:
            # Handle other filters based on their column names
            where_clause.append(f"{key} {'>=' if key.startswith('min_') else '<='} {value}")
        
    query = f"SELECT * FROM property_data WHERE {' AND '.join(where_clause)};"

    curs = conn.cursor()
    try:
        curs.execute(query)
        properties = curs.fetchall()
        curs.close()
    except Exception as e:
        curs.execute("ROLLBACK")
        conn.commit()
        return jsonify({'error': str(e)}), 400

    return jsonify(properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)