# Efficient Data Stream Anomaly Detection

## Project Overview

This project demonstrates an efficient method for detecting anomalies in a continuous data stream. The stream could represent various real-world metrics like financial transactions, system monitoring, etc. Anomalies are detected in real-time using an unsupervised K-Nearest Neighbors (KNN) algorithm.

### Objectives

1. **Algorithm Selection**: KNN is chosen as the algorithm for anomaly detection with a distance threshold to flag outliers.
2. **Data Stream Simulation**: The stream contains regular patterns (seasonality), noise, and trends.
3. **Real-time Anomaly Detection**: Anomalies are detected in real-time by training KNN on a sliding window of data.
4. **Optimization**: The model adapts to concept drift and noise by only using recent data in the sliding window.
5. **Visualization**: A live plot shows the data stream and the points flagged as anomalies.

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kamal030803/Data-Anomaly-Detector.git
   cd Efficient_Data_Stream_Anomaly_Detection
