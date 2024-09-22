from data_stream import generate_data_stream

if __name__ == "__main__":
    stream_length=1000
    seasonal_period=50
    noise_level=0.2
    window_size=50
    n_neighbors=5
    anomaly_threshold=1.2
    
    #Generating some random real data stream
    data_stream = generate_data_stream(length=stream_length, seasonal_period=seasonal_period, noise_level=noise_level)
