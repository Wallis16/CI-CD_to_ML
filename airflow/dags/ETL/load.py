from pymongo import MongoClient
from pyarrow import csv

def load_to_mongodb(username: str, password: str, database: str,
                     collection_name: str, table_path: str):

    # Replace with your MongoDB Atlas connection string
    mongo_uri = f'mongodb+srv://{username}:{password}@{database}.hi7evkw.mongodb.net/'

    # Connect to MongoDB Atlas
    client = MongoClient(mongo_uri)
    db = client[database]
    collection = db[collection_name]

    table = csv.read_csv(table_path)
    table = table.to_pandas()

    # Insert the data into MongoDB
    collection.insert_many(table.to_dict(orient = 'records'))

    # Close the MongoDB connection
    client.close()
