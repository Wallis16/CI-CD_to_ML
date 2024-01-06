from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import pandas as pd
import tensorflow as tf
import mlflow

def model_training(data_path, epochs):

    txt = []

    with open (data_path+'.dvc', 'r') as f:
        for line in f:
            txt.append(line)

    data_version = txt[1].split(': ')[-1][:-1]

    mlflow.set_tracking_uri('sqlite:///mlflow.db')
    mlflow.set_experiment(data_version)

    df = pd.read_csv(data_path)

    X = df.iloc[:,0:-1]
    y = df.iloc[:,[-1]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state = 42)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    with mlflow.start_run():

        mlflow.set_tag('Dataset', data_version)

        model = tf.keras.Sequential()

        model.add(tf.keras.layers.Dense(30))
        model.add(tf.keras.layers.Dense(60))
        model.add(tf.keras.layers.Dense(1))

        model.compile(
            loss = 'mse',
            optimizer = tf.keras.optimizers.Adam(),
            metrics = [tf.keras.metrics.RootMeanSquaredError(name='rmse')]
        )

        mlflow.tensorflow.autolog()

        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs)

        model_summary = []
        model.summary(print_fn=lambda x: model_summary.append(x))
        model_summary = '\n'.join(model_summary)

        mlflow.log_text(model_summary, 'model_summary.txt')
