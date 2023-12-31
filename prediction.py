import tensorflow as tf
import sqlite3
import numpy as np
import random
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score
import pandas as pd

RANDOM_SEED = 10


class SeafoodModel(tf.keras.Model):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ff = tf.keras.Sequential([
            tf.keras.layers.Dense(3, kernel_regularizer='l2', activation='leaky_relu'),
            tf.keras.layers.Dense(3, kernel_regularizer='l2', activation='leaky_relu'),
            tf.keras.layers.Dense(3, kernel_regularizer='l2', activation='leaky_relu'),
        ])
        self.final = tf.keras.layers.Dense(1, activation='sigmoid')



    def __call__(self, *args, **kwargs):
        inputs = args[0]

        return 5 * self.final(self.ff(inputs))


def min_max_scale(data):
    X_min = np.amin(data, axis=0)
    return (data - X_min) / (np.amax(data, axis=0) - X_min)

def train_test_split(X, Y, train_pct=0.8):
    """
    Input:
        - df: Pandas DataFrame
        - train_pct: optional, float
    Output:
        - train dataframe: Pandas DataFrame
        - test dataframe: Pandas DataFrame
    """
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    msk = np.random.rand(len(X)) < train_pct
    return X[msk], Y[msk], X[~msk], Y[~msk]


# ---------------------------------------------------------------------------------------


def main():
    conn = sqlite3.connect('./databases/wholeData.db')
    cur = conn.cursor()
    X = cur.execute('SELECT * FROM resturants')

    resturants = [list(i) for i in X]
    print(resturants[0])

    conn = sqlite3.connect('./databases/geolocation.db')
    cur = conn.cursor()
    X = cur.execute('SELECT * FROM geolocation')

    coords = [list(i) for i in X]
    coord_ids = [x[0] for x in coords]

    data = []

    for r in resturants:
        try:
            r_coords = coords[coord_ids.index(r[0])]
            r.extend(r_coords[-2:])
            data.append(r)

        except:
            pass

    data = [[x[3], x[4], x[6], x[7], x[9], x[10]] for x in data]
    price_dict = {p:i for i, p in enumerate(set([x[3] for x in data]))}
    
    used_data = [x[2:] for x in data]
    for x in used_data:
        x[1] = price_dict[x[1]]
    X = [x[1:] for x in used_data]
    Y = [x[0] for x in used_data]
    X = np.array(X)
    Y = np.array(Y)

    # X = np.array(tf.concat([X[:,1:], tf.one_hot(X[:,0], 5)], 1))
    X = X[:,1:]

    X = min_max_scale(X)

    # shuffle data
    indices = tf.range(0, len(X))
    indices = tf.random.shuffle(indices, seed=RANDOM_SEED)
    X = X[indices]
    Y = Y[indices]


    kf = KFold()
    kf.split(X, Y)
    accuracyTotal = 0
    linearAccuracy = 0
    for _, (train_index, test_index) in enumerate(kf.split(X)):


        X_train, Y_train, X_test, Y_test = X[train_index], Y[train_index], X[test_index], Y[test_index]


        nn_model = SeafoodModel()
        nn_model.compile(optimizer=tf.keras.optimizers.Adam(0.05), 
                        loss=tf.keras.losses.MeanSquaredError(), metrics=[tf.keras.metrics.MeanSquaredError()])
        nn_model.fit(X_train, Y_train, epochs=10, validation_data=(X_test, Y_test))

        _, accuracy = nn_model.evaluate(X_test, Y_test)
        accuracyTotal += accuracy

        regression_model = Ridge(alpha=0.1).fit(X_train, Y_train)
        y_pred = regression_model.predict(X_test)

        accuracy = r2_score(Y_test, y_pred)
        linearAccuracy += accuracy


    print("Average Accuracy = {:.2f}".format(accuracyTotal/5))
    print("Average Accuracy of Ridge regression model: ", linearAccuracy/5)

if __name__ == '__main__':
    main()
