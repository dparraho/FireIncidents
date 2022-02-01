FROM apache/airflow:2.2.3

LABEL maintainer="Daniel Parra"

ENV AIRFLOW_HOME=/opt/airflow

COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
COPY create_cnx.sh ${AIRFLOW_HOME}/create_cnx.sh

WORKDIR ${AIRFLOW_HOME}