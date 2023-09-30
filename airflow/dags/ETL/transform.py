import pyarrow.compute as compute

from pyarrow import csv

def transform_data(selected_columns: list, transform_path: str, data_staging_path: str,
               table_path: str) -> str:

    table = csv.read_csv(table_path)
    table = table.select(selected_columns)

    schema = table.schema
    column_names = schema.names

    # Iterate through each column and count non-null values
    for column_name in column_names:
        # Use the `is_valid` function to check for non-null values
        non_null_count = compute.count(table[column_name])
        print(f"Column '{column_name}' has {non_null_count} non-null values.")

    csv.write_csv(table, data_staging_path+transform_path)
    return data_staging_path+transform_path
