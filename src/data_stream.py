import numpy as np

def generate_data_stream(length=1000, seasonal_period=100, noise_level=0.1, normalize = True):
    """Generates a stream of data with seasonal variations and noise."""
    
    time = np.arange(0, length)
    #seasonal component
    seasonal = np.sin(2 * np.pi * time / seasonal_period)  
    
    #random noise
    noise = np.random.normal(0, noise_level, length)  
    
    #gradual upward trend
    trend = np.linspace(0, 2, length) 
     
    data = seasonal + noise + trend
    
    if normalize:
        data = (data-np.mean(data))/np.std(data)
    return data

