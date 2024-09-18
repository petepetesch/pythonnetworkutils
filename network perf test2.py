import speedtest
import time
TrackSpeeds = []
numIterations = 20


def test_network_performance():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")
    TrackSpeeds.append(float(download_speed))
    print()

if __name__ == "__main__":
    for i in range(0,numIterations):
        test_network_performance()
        time.sleep(60)

print()
print("Track Speeds \n")
print(TrackSpeeds)
print("Minimum performance:")
print(min(TrackSpeeds))
print()
print("Max Performance")
print(max(TrackSpeeds))
print()
print("Average Performance")
print(sum(TrackSpeeds)/numIterations)
