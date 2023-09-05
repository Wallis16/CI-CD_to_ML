from pymongo import MongoClient
from dotenv import load_dotenv

import pandas as pd
import os

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
username = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")
database = os.getenv("MONGODB_DATABASE")
collection_name = os.getenv("MONGODB_COLLECTION")

# Replace with your MongoDB Atlas connection string
mongo_uri = f"mongodb+srv://{username}:{password}@{database}.dczmvwe.mongodb.net/"

# Read the CSV file into a DataFrame
csv_file = 'transform_data.csv'

#table = csv.read_csv(csv_file)
table = pd.read_csv(csv_file)

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client[database]
collection = db[collection_name]

# Insert the data into MongoDB
collection.insert_many(table.to_dict(orient = "records"))

# Close the MongoDB connection
client.close()