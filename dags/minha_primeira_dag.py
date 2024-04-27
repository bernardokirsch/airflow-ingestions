from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'bernardo_kirsch',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 22),
    'retries': 0,
    }

with DAG(
    'minha_primeira_dag',
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    default_args=default_args
    ) as dag:

    t1 = BashOperator(
    task_id='primeiro_etl',
    bash_command="""
    cd /opt/airflow/dags/etl_scripts/
    python /opt/airflow/dags/etl_scripts/meu_primeiro_script_etl.py
    """)

    t2 = BashOperator(
    task_id='segundo_etl',
    bash_command="""
    python /opt/airflow/dags/etl_scripts/meu_segundo_script_etl.py
    """)

    t1 >> t2