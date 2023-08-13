# General imports for Airflow
from airflow.decorators import dag, task
from datetime import datetime, timedelta

# Utility imports
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

@dag(
    
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['retail'],
)

def retail():
    
    # This task will upload the csv file to GCS bucket
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='include/dataset/online_retail.csv',
        dst='raw/online_retail.csv',
        bucket='dataset_online_retail',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )
    
    # This task will create a dataset in BigQuery
    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_retail_dataset',
        dataset_id='retail',
        gcp_conn_id='gcp',
    )
    
retail()