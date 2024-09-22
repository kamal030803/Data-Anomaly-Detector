from data_stream import generate_data_stream
from knn_anomaly_detector import KNNAnomalyDetector
from visualize import visualize_stream

if __name__ == "__main__":
    stream_length=1000
    seasonal_period=50
    noise_level=0.2
    window_size=50
    n_neighbors=3
    threshold_percentile = 99
    
    #Generating some random real data stream
    data_stream = generate_data_stream(length=stream_length, seasonal_period=seasonal_period, noise_level=noise_level)
    
    knn_detector = KNNAnomalyDetector(window_size=window_size, n_neighbors=n_neighbors, threshold_percentile=threshold_percentile)

    #anomalies for this PoC
    anomalies = {}
    for i, point in enumerate(data_stream):
        is_anomaly, distance = knn_detector.detect_anomaly(point)
        if is_anomaly:
            anomalies[i] = point
        print(f"Time {i}: Value {point}, Anomaly: {is_anomaly}, Distance: {distance}")
    visualize_stream(data_stream, anomalies)