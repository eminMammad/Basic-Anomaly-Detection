import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulate_data import simulate_bitcoin_price_stream
from detect_anomalies import detect_anomalies_in_stream 


# Real-time plotting with matplotlib
def plot_real_time_data_and_anomalies():
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    anomaly_x, anomaly_y = [], []

    line, = ax.plot([], [], lw=2, label='Price')
    anomaly_points, = ax.plot([], [], 'ro', label='Anomaly')

    ax.set_xlim(-100, 100)
    ax.set_ylim(10000, 40000)
    ax.set_title("Bitcoin Price Stream with Anomalies")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")

    def update(frame):
        x_data.append(frame[0])
        y_data.append(frame[1])
        
        if frame[2]:  # If anomaly detected
            anomaly_x.append(frame[0])
            anomaly_y.append(frame[1])
            anomaly_points.set_data(anomaly_x, anomaly_y)
        else:
            line.set_data(x_data, y_data)

        ax.set_xlim(max(0, frame[0] - 100), frame[0] + 10)
        ax.set_ylim(min(y_data[-100:], default=0), max(y_data[-100:], default=40000) + 1000)

        return line, anomaly_points
    window_size = 20
    price_stream = simulate_bitcoin_price_stream(interval=1, noise_level=5)
    anomaly_stream = detect_anomalies_in_stream(price_stream, window_size, threshold=2)

    def data_gen():
        for i, (price, state) in enumerate(anomaly_stream):
            yield i,price,state

    ani = FuncAnimation(fig, update, frames=data_gen, interval=5000, blit=True)
    plt.legend()
    plt.show()

# Run the plot
if __name__ == "__main__":
    plot_real_time_data_and_anomalies()
