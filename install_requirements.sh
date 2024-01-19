#!/bin/bash

# Update package index
sudo apt update

# Install PostgreSQL and its contrib package
sudo apt install postgresql postgresql-contrib -y

# Execute the following commands as the postgres user
sudo -u postgres psql <<EOF

-- Create a new user
CREATE USER testuser;

-- Give permission to the new user for creating database
ALTER ROLE testuser CREATEDB;

-- Set up a password for the new user
ALTER USER testuser PASSWORD 'temppassword';

-- Create a new database
CREATE DATABASE state_district;

-- Grant all privileges on the database to the new user
GRANT ALL PRIVILEGES ON DATABASE state_district TO testuser;

EOF

echo "PostgreSQL installation and initial setup complete."

pip3 install SQLAlchemy openpyxl psycopg2-binary

echo "Required Packages are installed."
