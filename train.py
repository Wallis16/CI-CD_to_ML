from pymongo import MongoClient
from dotenv import load_dotenv

import os
import pandas as pd

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
username = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")
database = os.getenv("MONGODB_DATABASE")
collection_name = os.getenv("MONGODB_COLLECTION")

# Replace with your MongoDB Atlas connection string
mongo_uri = f"mongodb+srv://{username}:{password}@{database}.dczmvwe.mongodb.net/"

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client[database]
collection = db[collection_name]

# Use find() to retrieve all documents in the collection
cursor = collection.find()

# Convert documents to a list of dictionaries
documents_list = list(cursor)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(documents_list)