import speedtest
import time
TrackSpeeds = []


def test_network_performance():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")
    TrackSpeeds.append(download_speed)
    print()

if __name__ == "__main__":
    for i in range(0,5):
        test_network_performance()
        time.sleep(60)

print()
print("Track Speeds \n")
print(TrackSpeeds)
print("Minimum performance:")
min(TrackSpeeds)
print()
print("Max Performance")
max(TrackSpeeds)
