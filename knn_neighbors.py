import numpy as np
import sqlite3
from sklearn.neighbors import KNeighborsRegressor
import tensorflow as tf

def fetch_data(query, db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            return cur.execute(query).fetchall()
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

def preprocess_data(prices, longitudes, latitudes):
    price_mapping = {'N/A': 2, '$': 1, '$$': 2, '$$$': 3, '$$$$': 4}
    prices_num = np.array([price_mapping.get(price[0], 2) for price in prices])
    prices_one_hot = tf.one_hot(prices_num, depth=5).numpy() * 0.9
    return np.hstack((prices_one_hot, np.array(longitudes), np.array(latitudes)))

def train_and_predict(X_train, y_train, X_test, new_location):
    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    mse = np.mean((y_test - y_pred) ** 2)
    predicted_rating = knn.predict(new_location)[0]
    return mse, predicted_rating

def main():
    prices = fetch_data('SELECT price FROM resturants', './databases/wholeData.db')
    longitudes = fetch_data('SELECT longitude FROM geolocation', './databases/geolocation.db')
    latitudes = fetch_data('SELECT latitude FROM geolocation', './databases/geolocation.db')
    ratings = fetch_data('SELECT rating FROM resturants', './databases/wholeData.db')

    X = preprocess_data(prices, longitudes, latitudes)
    y = np.array([rating[0] for rating in ratings])

    split_idx = int(0.8 * len(X))
    X_train, y_train = X[:split_idx], y[:split_idx]
    X_test, y_test = X[split_idx:], y[split_idx:]

    mse, predicted_rating = train_and_predict(X_train, y_train, X_test, [[1, 1, 0, 0, 2.1, 20.1]])

    print("Mean squared error:", mse)
    print("Predicted rating for new location:", predicted_rating)

if __name__ == '__main__':
    main()
