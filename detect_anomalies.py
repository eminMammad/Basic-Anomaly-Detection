from utils import calculate_mean, calculate_standard_deviation

def sliding_window(data_stream, window_size):
    """
    Generate a sliding window over a data stream.

    Parameters:
    - data_stream: An iterable sequence of data.
    - window_size: The size of the sliding window.

    Yields:
    - Lists of data points within the sliding window.
    """
    window = []
    for x in data_stream:
        window.append(x)
        if len(window) > window_size:
            window.pop(0)
        yield list(window)  # Yield the window even if it's not full yet

def detect_anomalies_in_stream(stream, window_size=30, threshold=3):
    """
    Detect anomalies in a data stream using a sliding window approach, returning values even
    before the sliding window is full (without anomaly detection).

    Parameters:
    - stream: The data stream to process.
    - window_size: The size of the window used for anomaly detection.
    - threshold: The threshold for detecting anomalies (in terms of standard deviations).

    Yields:
    - (latest_point, anomaly_detected): The latest point in the stream and whether it's an anomaly.
    """
    windowed_stream = sliding_window(stream, window_size)

    for window in windowed_stream:
        anomaly_detected = False

        if len(window) < window_size:
            # Window not yet full, yield the current value without checking for anomalies
            latest_point = window[-1]  # Get the most recent value
            yield latest_point, anomaly_detected  # False anomaly detection because window isn't full yet
        else:
            # Full window, proceed with anomaly detection
            mean = calculate_mean(window[:-1])  # Exclude the last point from the mean calculation
            std_dev = calculate_standard_deviation(window[:-1])  # Exclude the last point from the standard deviation calculation

            latest_point = window[-1]  # Check the most recent value

            # If the latest point deviates from the mean by more than threshold * std_dev, it's an anomaly
            if abs(latest_point - mean) > threshold * std_dev:
                print(f"Anomaly detected! Value: {latest_point}, Mean: {mean}, Std Dev: {std_dev}")
                anomaly_detected = True
            else:
                print(f"Normal value: {latest_point}, Mean: {mean}, Std Dev: {std_dev}")
            
            yield latest_point, anomaly_detected
