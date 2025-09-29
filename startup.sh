#!/bin/bash

# Initialize the Airflow database (only if not already initialized)
airflow db init

# Create admin user (only if it doesn't exist)
airflow users create \
  --username airflow \
  --firstname Air \
  --lastname Flow \
  --role Admin \
  --email airflow@example.com \
  --password airflow || true

# Start the Airflow webserver
exec airflow webserver
