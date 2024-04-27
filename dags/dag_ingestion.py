from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable

default_args = {
    'owner': 'bernardo_kirsch',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 25),
    'retries': 0,
}

with DAG(
    'dag_ingestion',
    schedule_interval=timedelta(minutes=0.5),
    catchup=False,
    default_args=default_args
) as dag:

    t1 = BashOperator(
        task_id='ingestion_t1',
        bash_command="""
        python /opt/airflow/dags/ingestion_scripts/ingestion_t1.py
        """
    )

    t2 = BashOperator(
        task_id='ingestion_t2',
        bash_command="""
        python /opt/airflow/dags/ingestion_scripts/ingestion_t2.py
        """,
        env={'RESULTADO_PATH': Variable.get('resultado_path')}
    )

    t1 >> t2