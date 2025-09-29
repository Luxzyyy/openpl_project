#!/bin/bash
set -e

# Initialize the DB
airflow db migrate

# Create Airflow user only if it doesn't exist
if ! airflow users list | grep -q airflow; then
  airflow users create \
    --username airflow \
    --firstname Air \
    --lastname Flow \
    --role Admin \
    --email airflow@example.com \
    --password airflow
fi

# Start the scheduler in the background
airflow scheduler &

# Start the webserver (in foreground)
exec airflow webserver
