# State and District Data Importer

## Overview
This project automates the process of setting up a PostgreSQL database and importing state and district data from an Excel file into the database.

## Files
- `install_requirements.sh`: Bash script to install PostgreSQL, create a database, a user and install python packages.
- `save_data_postgre.py`: Python script to import data from an Excel file into the PostgreSQL database.
- `state_district.xlsx`: Excel file containing the data to be imported, with two sheets: 'state' and 'district'.

## Prerequisites
- Linux-based system
- Python 3
- pandas and SQLAlchemy libraries for Python
- PostgreSQL

## Installation and Setup
1. **Install PostgreSQL and Python Package:**
   - Run `install_requirements.sh` to install PostgreSQL and set up the database, user and install python packages.
   ```sh
   sudo chmod +x install_requirements.sh
   ./install_requirements.sh
   ```

## Usage
1. **Run the Python Script:**
   - Execute `save_data_postgre.py` to import the data from `state_district.xlsx` into the PostgreSQL database.
   ```sh
   python save_data_postgre.py
   ```
