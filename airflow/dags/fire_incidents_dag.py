from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# from fire_incidents_etl import run_fire_incidents_etl
from etl import IngestRaw

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
    'fire_dag',
    catchup=False,
    default_args=default_args,
    description='DAG with ETL process',
    schedule_interval=timedelta(days=1),
)


def run():
    job = IngestRaw()
    job.download()
    print("descarga exitosa")
    job.transform()
    print("transformacion exitosa")
    job.load_to_postgres()
    print("Carga exitosa")

run_etl = PythonOperator(
    task_id='whole_fire_incidents_etl',
    python_callable=run,
    dag=dag,
)

run_etl