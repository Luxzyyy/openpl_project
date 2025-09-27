FROM apache/airflow:2.8.1-python3.9

USER airflow
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

ENV AIRFLOW_HOME=/opt/airflow

COPY dags/ /opt/airflow/dags/
COPY src/ /opt/airflow/src/
COPY .env /opt/airflow/.env

EXPOSE 8080
CMD ["airflow", "webserver"]