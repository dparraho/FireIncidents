#!/bin/sh

airflow connections \
    --add \
    --conn_id postgres_datawarehouse \
    --conn_type postgres \
    --conn_login ${POSTGRES_USER} \
    --conn_password ${POSTGRES_PASS} \
    --conn_port ${PG_PORT} \
    --conn_host ${PG_HOST} \
    --conn_schema ${POSTGRES_DB}
