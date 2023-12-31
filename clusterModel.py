import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class KMeans:
    def __init__(self, X, K, max_iters):
        self.X = X
        self.K = K
        self.max_iters = max_iters
        self.centroids = self.init_centroids()

    def init_centroids(self):
        np.random.seed(42)  # For reproducibility
        return self.X[np.random.choice(self.X.shape[0], self.K, replace=False)]

    def euclidean_dist(self, x, y):
        return np.sqrt(np.sum((x - y) ** 2, axis=1))

    def closest_centroids(self):
        distances = np.array([self.euclidean_dist(x, self.centroids) for x in self.X])
        return np.argmin(distances, axis=1)

    def compute_centroids(self, indices):
        new_centroids = np.array([self.X[indices == i].mean(axis=0) for i in range(self.K)])
        if np.allclose(self.centroids, new_centroids):
            return True
        else:
            self.centroids = new_centroids
            return False

    def run(self):
        for _ in range(self.max_iters):
            indices = self.closest_centroids()
            if self.compute_centroids(indices):
                break
        return self.centroids, indices

    def inertia(self, centroids, indices):
        return sum(self.euclidean_dist(self.X[i], centroids[idx]) ** 2 for i, idx in enumerate(indices))

def get_data_from_db(query, db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            return cur.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []

def preprocess_data(data, region_mapping):
    scaler = MinMaxScaler()
    return scaler.fit_transform(np.array([[region_mapping.get(item[0], 8), float(item[1])] for item in data]))

def plot_elbow_point(cluster_range, errors):
    plt.plot(cluster_range, errors)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method Plot')
    plt.show()

MAX_CLUSTERS = 10

def main():
    REGION_MAPPING = {'South': 0, 'North': 1, 'East': 2, 'West': 3, 'Northeast': 4,
                      'Northwest': 5, 'Southeast': 6, 'Southwest': 7, 'Unknown': 8}
    
    ocean_data = get_data_from_db('SELECT region, distance FROM oceanDistance', './databases/oceanDistance.db')
    rating_data = get_data_from_db('SELECT rating FROM resturants', './databases/wholedata.db')

    ocean_data = preprocess_data(ocean_data, REGION_MAPPING)
    rating_data = preprocess_data(rating_data, {'N/A': 2, '$': 1, '$$': 2, '$$$': 3, '$$$$': 4})

    X = np.hstack((ocean_data, rating_data))

    inertias = []
    for i in range(1, MAX_CLUSTERS + 1):
        k_means = KMeans(X, i, max_iters=25)
        centroids, indices = k_means.run()
        inertia_val = k_means.inertia(centroids, indices)
        inertias.append(inertia_val)

    plot_elbow_point(range(1, MAX_CLUSTERS + 1), inertias)

if __name__ == '__main__':
    main()
