from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from main import main

default_args = {
    'start_date': datetime(2025, 9, 28),
    'retries': 1,
}

with DAG(
    dag_id="example_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:

    run_main = PythonOperator(
        task_id="run_main",
        python_callable=main
    )