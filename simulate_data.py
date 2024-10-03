import time
import requests
import math
import numpy as np
import random
# Fetch data from an external CoinGecko API  
def fetch_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",  
        "vs_currencies": "usd"
    }
    # try: 
    #     response = requests.get(url, params=params)
    # except Exception as e:
    #     return None 

    return  random.randint(50000,60000) # response.json()['bitcoin']['usd'] if response.status_code == 200  else None
    
def data_stream_from_api(poll_interval=2):
    while True:
        price = fetch_data() #int(input()) #fetch_data()
        if price:
            yield price
        time.sleep(poll_interval)  # Wait for the defined interval before fetching again


def simulate_bitcoin_price_stream(interval=5, noise_level=0.01):
    """
    Simulate real-time Bitcoin prices with regular patterns, seasonal elements, and random noise.
    
    Parameters:
    - duration: Total time to simulate (in seconds).
    - interval: Time interval between API calls (in seconds).
    - noise_level: The scale of the random noise (as a fraction of the price).
    
    Yields:
    - A simulated Bitcoin price point.
    """
    start_time = time.time()

    while True:
        # Fetch the real Bitcoin price from the API
        base_price = next(data_stream_from_api())
        
        if base_price:
            current_time = time.time() - start_time
            
            # Regular pattern (trend): Linear drift in price (e.g., 0.1% increase per minute)
            trend = base_price * (0.001 * current_time / 60)
            print("Trend: ", trend) 
            # Seasonal pattern (e.g., sinusoidal fluctuation every 30 seconds)
            seasonality = abs(base_price * 0.02 * math.sin(2 * math.pi * current_time / 30))
            print("Seasonality: ", seasonality) 
            # Random noise as a small percentage of the current price
            noise = abs(base_price * np.random.normal(0, noise_level))
            print("Noise: ", noise)
            # Simulated price combining base price, trend, seasonality, and noise
            simulated_price = base_price + trend + seasonality + noise
            print("Simulated Price: ",simulated_price)
            yield simulated_price  # Fetch every 5 seconds
        
        # time.sleep(interval)