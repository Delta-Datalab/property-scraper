import os
from flask import Flask, jsonify
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

@app.route('/locations')
def get_locations():
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT location FROM property_data ORDER BY location ASC;")
    locations = [row[0] for row in cur.fetchall()]  # Extract location values
    cur.close()
    return jsonify({'locations': locations})

@app.route('/')
def hello_world():
    cur = conn.cursor()  # Create a cursor for database operations
    # Example query (replace with your actual queries)
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    return f'Hello, World! PostgreSQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
