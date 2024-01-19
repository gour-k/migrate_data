import pandas as pd
from sqlalchemy import create_engine, text

# Load data from the Excel file
file_path = 'state_district.xlsx'
df_states = pd.read_excel(file_path, sheet_name='state')
df_districts = pd.read_excel(file_path, sheet_name='district')

# PostgreSQL connection parameters
dbname = 'state_district' # Database name
user = 'testuser' # Username
password = 'temppassword' # Password
host = '127.0.0.1' # Host
port = '5432' # Port

# Create a connection to the database
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Create table for state data
create_states_table_query = text('''
CREATE TABLE IF NOT EXISTS states (
    state_id INTEGER PRIMARY KEY,
    state_union_territory VARCHAR(255),
    number_of_districts INTEGER,
    population BIGINT,
    population_per_district BIGINT,
    type VARCHAR(50)
)
''')

# Create table for district data
create_districts_table_query = text('''
CREATE TABLE IF NOT EXISTS districts (
    district_id INTEGER PRIMARY KEY,
    district VARCHAR(255),
    headquarters VARCHAR(255),
    population BIGINT,
    area_km2 FLOAT,
    density_per_km2 FLOAT,
    state_id INTEGER REFERENCES states(state_id)
)
''')

# Connect and create tables if not exist
with engine.connect() as connection:
    connection.execute(create_states_table_query)
    connection.execute(create_districts_table_query)

# Insert data into the tables
df_states.to_sql('states', engine, if_exists='append', index=False)
df_districts.to_sql('districts', engine, if_exists='append', index=False)

print("Data has been successfully inserted into the database.")