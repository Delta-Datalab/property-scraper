import os

LOG_DIR = os.path.join(os.getcwd(),'logs','property_data.log') 
DATA_DIR = os.path.join(os.getcwd(),'data')
OUTPUT_DATA_DIR = os.path.join(DATA_DIR, 'data.csv')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)