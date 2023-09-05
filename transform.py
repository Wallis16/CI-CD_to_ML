from pyarrow import csv
import pyarrow.compute as compute

table = csv.read_csv("house_rent_dataset.csv")

schema = table.schema
column_names = schema.names

# Iterate through each column and count non-null values
for column_name in column_names:
    # Use the `is_valid` function to check for non-null values
    non_null_count = compute.count(table[column_name])
    print(f"Column '{column_name}' has {non_null_count} non-null values.")

csv.write_csv(table, "transform_data.csv")

