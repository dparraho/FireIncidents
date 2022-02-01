from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import pandas as pd
from models import FireIncidents
from sodapy import Socrata
from utils import get_session
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['dparraho@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'test_session_dag',
    catchup=False,
    default_args=default_args,
    description='DAG for test proccess',
    schedule_interval=timedelta(days=1),
)


def run():
    # with get_session() as (session, _):
    #     session.execute("""
    #         CREATE TABLE IF NOT EXISTS DUMMY_2022_01_31
    #         PARTITION OF raw.fire_incidents
    #         FOR VALUES FROM ('2022-01-31') to ('2022-02-01')
    #         """)
    #     session.commit()
    # data = pd.read_csv(os.environ["SOURCE_URL"])
    def get_data_client():
        client = Socrata("data.sfgov.org", os.environ["APP_TOKEN"])
        results = client.get("wr8u-xric", limit=20)
        data = pd.DataFrame.from_records(results)
        data = data.astype(str)
        data.columns = data.columns.str.replace("_", " ").str.title().str.replace(" ", "")
        return data

    def get_data_url():
        data = pd.read_csv(os.environ["SOURCE_URL"])
        data = data.astype(str)
        data.columns = data.columns.str.replace(" ", "")
        return data

    data_dict = get_data_url().to_dict('records')
    print(data_dict)
    with get_session() as (session, _):
        for d in data_dict:
            row = FireIncidents(**d)
            session.add(row)
        session.commit()




run_etl = PythonOperator(
    task_id='whole_fire_incidents_etl',
    python_callable=run,
    dag=dag,
)

run_etl