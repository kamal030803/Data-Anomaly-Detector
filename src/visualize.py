import matplotlib.pyplot as plt

def visualize_stream(data, anomalies):
    """Visualizes the data stream with detected anomalies."""
    plt.figure(figsize=(10, 6))
    plt.plot(data, label="Data Stream")
    plt.scatter(anomalies.keys(), anomalies.values(), color='r', label="Anomalies", zorder=5)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Real-Time Data Stream with Anomalies')
    plt.legend()
    plt.grid(True)
    plt.show()