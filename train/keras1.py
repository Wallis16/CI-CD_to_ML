from pymongo import MongoClient
from dotenv import load_dotenv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import os
import pandas as pd
import tensorflow as tf
import mlflow

mlflow.set_tracking_uri('sqlite:///mlflow.db')
mlflow.set_experiment('house-rent')

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
database = os.getenv('MONGODB_DATABASE')
collection_name = os.getenv('MONGODB_COLLECTION')

# Replace with your MongoDB Atlas connection string
mongo_uri = f'mongodb+srv://{username}:{password}@{database}.dczmvwe.mongodb.net/'

txt = []

with open ('transform_data.csv.dvc', 'r') as f:
    for line in f:
        txt.append(line)

data_version = txt[1].split(': ')[-1][:-1]

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

X = df[['BHK','Size','Bathroom']]
y = df['Rent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state = 42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

with mlflow.start_run():

    mlflow.set_tag('Dataset', data_version)

    model = tf.keras.Sequential()

    model.add(tf.keras.layers.Dense(30))
    model.add(tf.keras.layers.Dense(60))
    model.add(tf.keras.layers.Dense(60))
    model.add(tf.keras.layers.Dense(60))
    model.add(tf.keras.layers.Dense(1))

    model.compile(
        loss = 'mse',
        optimizer = tf.keras.optimizers.Adam(),
        metrics = [tf.keras.metrics.RootMeanSquaredError(name='rmse')]
    )

    mlflow.tensorflow.autolog()

    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20)

    model_summary = []
    model.summary(print_fn=lambda x: model_summary.append(x))
    model_summary = '\n'.join(model_summary)

    mlflow.log_text(model_summary, 'model_summary.txt')
