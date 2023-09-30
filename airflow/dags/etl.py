from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

from dotenv import load_dotenv

from ETL.extract import download_from_drive
from ETL.transform import transform_data
from ETL.load import load_to_mongodb

import os

load_dotenv()

url_data = os.getenv('URL_DATA')
output_name_extract = os.getenv('OUTPUT_NAME_EXTRACT')
output_name_transform = os.getenv('OUTPUT_NAME_TRANSFORM')
data_staging_path = os.getenv('DATA_STAGING')

# Access the environment variables
username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
database = os.getenv('MONGODB_DATABASE')
collection_name = os.getenv('MONGODB_COLLECTION')

default_args = {
    'owner': 'diogenes',
    'start_date': days_ago(1),
}

@task()
def extract(url_data, output_name, data_staging_path):
    return download_from_drive(url_data, output_name, data_staging_path)

@task()
def transform(selected_columns, transform_path, data_staging_path, table_path):
    return transform_data(selected_columns, transform_path, data_staging_path, table_path)

@task()
def load(username, password, database, collection_name, transform_data_path):
    load_to_mongodb(username, password, database, collection_name, transform_data_path)

with DAG(dag_id = 'etl', schedule_interval='@once',
         default_args=default_args, catchup=False) as dag:

    extract_data_path = extract(url_data, output_name_extract, data_staging_path)
    transform_data_path = transform(['BHK','Size','Bathroom','Rent'], output_name_transform,
                                    data_staging_path, extract_data_path)
    load(username, password, database, collection_name, transform_data_path)
