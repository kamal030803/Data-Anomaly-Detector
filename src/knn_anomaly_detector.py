import numpy as np
from sklearn.neighbors import NearestNeighbors
from collections import deque

class KNNAnomalyDetector:
    def __init__(self, window_size=100, n_neighbors=5, threshold=1.5):
        self.window_size=window_size
        self.n_neighbors=n_neighbors
        self.threshold=threshold
        self.data_window=deque(maxlen=window_size)

    def fit_knn(self):
        """Train KNN model on the current window of data."""
        if len(self.data_window) < self.window_size:
            return
        data = np.array(self.data_window).reshape(-1, 1)
        self.knn_model = NearestNeighbors(n_neighbors=self.n_neighbors)
        self.knn_model.fit(data)

    def detect_anomaly(self, new_point):
        """Detect if the new point is an anomaly based on KNN distance."""
        self.data_window.append(new_point)
        if len(self.data_window) < self.window_size:
            return False, None

        self.fit_knn()
        distances, _ = self.knn_model.kneighbors([[new_point]])
        avg_distance = np.mean(distances)

        if avg_distance > self.threshold:
            return True, avg_distance
        return False, avg_distance
