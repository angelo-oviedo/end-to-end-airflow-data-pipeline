from airflow.decorators import dag, task
from datetime import datetime, timedelta

@dag(
    
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['retail'],
)

def retail():
    
retail()