FROM apache/airflow:2.8.1-python3.9

USER airflow

# Install Python dependencies as airflow user
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH="/opt/airflow/src"

# Copy project files
COPY --chown=airflow:root dags/dags.py /opt/airflow/dags
COPY src/ ${AIRFLOW_HOME}/src/
COPY .env ${AIRFLOW_HOME}/.env

# Go back to root to copy entrypoint
USER root
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Force Docker container to prefer IPv4 over IPv6
RUN echo 'precedence ::ffff:0:0/96  100' >> /etc/gai.conf


# Run as airflow user again
USER airflow

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8080



