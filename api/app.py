import os
from flask import Flask, jsonify, request
import psycopg2  # Import the psycopg2 library for PostgreSQL

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

@app.route('/')
def hello_world():
    cur = conn.cursor()  # Create a cursor for database operations
    # Example query (replace with your actual queries)
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    return f'Hello, World! PostgreSQL version: {version[0]}'

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

@app.route('/properties/location/<location>')
def get_properties_by_location(location):
    cur = conn.cursor()
    cur.execute("SELECT * FROM property_data WHERE location = %s;", (location,))
    properties = cur.fetchall()
    cur.close()

    return jsonify(properties)


# curl http://localhost:5000/properties/filter?min_price=150000&max_price=250000&min_bedrooms=2&location=City%20A
@app.route('/properties/filter')
def get_properties_by_filter():
    filters = {}  # Initialize an empty dictionary for filters
    for key, value in request.args.items():
        if key in ('min_price', 'max_price', 'min_bedrooms', 'max_bathrooms', 'location', 'has_parking'):
            try:
                # Attempt to convert value to appropriate data type
                value = float(value) if key in ('min_price', 'max_price', 'min_bedrooms', 'max_bathrooms') else str(value)
                filters[key] = value
            except ValueError:
                return jsonify({'error': 'Invalid value for filter: {}'.format(key)}), 400

    # Build the SQL query dynamically based on provided filters
    where_clause = []
    for key, value in filters.items():
        if key == 'location':
            where_clause.append(f"location = '{value}'")
        else:
            where_clause.append(f"{key} {'>=' if key.startswith('min_') else '<='} {value}")

    query = f"SELECT * FROM property_data WHERE {' AND '.join(where_clause)};"

    cur = conn.cursor()
    cur.execute(query)
    properties = cur.fetchall()
    cur.close()

    return jsonify(properties)


# curl -X POST http://localhost:5000/properties -H "Content-Type: application/json" -d '{"price": 250000, "location": "City B", "bedrooms": 3, "bathrooms": 2}'
# Import requests
# data = {
#     "price": 300000,
#     "location": "Town C",
#     "bedrooms": 4,
#     "bathrooms": 2.5,
#     # ... other property details
# }

# response = requests.post("http://localhost:5000/properties", json=data)

# if response.status_code == 201:
#     print("Property created successfully!")
# else:
#     print("Error:", response.status_code, response.text)

@app.route('/properties', methods=['POST'])
def create_property():
    data = request.get_json()  # Get the JSON payload

    # Validate and extract necessary data (replace with your specific validation logic)
    price = data.get('price', None)
    location = data.get('location', None)
    # ... (extract other required data)

    if not all([price, location, ...]):  # Check for missing fields
        return jsonify({'error': 'Missing required fields'}), 400

    # Prepare SQL query to insert new property (adjust column names accordingly)
    query = "INSERT INTO property_data (price, location, ...) VALUES (%s, %s, ...);"

    cur = conn.cursor()
    cur.execute(query, (price, location, ...))
    conn.commit()  # Commit the changes
    cur.close()

    return jsonify({'message': 'Property added successfully'}), 201


# curl -X PUT http://localhost:5000/properties/1 -H "Content-Type: application/json" -d '{"price": 350000, "location": "Town D"}'
# Update price and description for property with ID 2:
# property_id = 2
# data = {
#     "price": 400000,
#     "description": "Newly renovated with modern amenities."
# }

# response = requests.put(f"http://localhost:5000/properties/{property_id}", json=data)

# if response.status_code == 200:
#     print("Property updated successfully!")
# else:
#     print("Error:", response.status_code, response.text)
@app.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    data = request.get_json()

    # Validate and extract updated data (replace with your validation logic)
    price = data.get('price', None)
    location = data.get('location', None)
    # ... (extract other updated data)

    # Prepare SQL query to update property (adjust column names and conditions)
    query = "UPDATE property_data SET price=%s, location=%s, ... WHERE id=%s;"

    cur = conn.cursor()
    cur.execute(query, (price, location, ..., property_id))
    conn.commit()
    cur.close()

    return jsonify({'message': 'Property updated successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)