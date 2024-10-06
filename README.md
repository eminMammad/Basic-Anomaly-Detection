# Standard Deviation for Anomaly Detection in Data Streams

In my project, I used the standard deviation to detect anomalies in data streams. The standard deviation is a statistical measure that quantifies the amount of variation or dispersion in a dataset. It is a useful tool for detecting anomalies because it can identify data points that are significantly different from the rest of the data.

1. **Simplicity**: The standard deviation is a simple statistical measure that doesn't require complex computations. It's easy to understand and implement.

2. **Efficiency**: The standard deviation can be computed in a single pass over the data, making it suitable for real-time anomaly detection in data streams.

# Explanation of the Code
In the code, window_size is declared as 20, we use these data to calculate initial mean and std_dev values. Subsequent data points are then checked against these values to detect anomalies. If a data point is more than 3 standard deviations (or any given threshold value) away from the mean, it is considered as an anomaly. Window size and threshold values are abstracted from the user. If needed, modifications can be made in the **detect_anomalies.py** file.

# How to Run the Code
After installing required packages with:
```python
pip install -r requirements.txt
```
You can run the code by executing the following command in your terminal:

```bash
python visualization.py
```

# Important Note
CoinGecko API is used to get the data. Because of slow API responses, floating data artificially created with random library. If you want to use the real time data, you can uncomment code related to API requests  in the **fetch_data()** function of **simulate_data.py** file.
