import speedtest
import time
TrackSpeeds = []
LatencySpeeds = []
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
    LatencySpeeds.append(float(ping))
    print()

def updatestats(k):
    print()
    k=k+1
    print("Iteration#  "+ str(k))
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
    print(sum(TrackSpeeds)/k)
    print()
    print("Average Latency/Ping")
    print(sum(LatencySpeeds)/k)

if __name__ == "__main__":
    for i in range(0,numIterations):
        test_network_performance()
        updatestats(i)
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
print()
print("Minimum latency:")
print(min(LatencySpeeds))
print()
print("Max Latency")
print(max(LatencySpeeds))
print()
print("Average Latency")
print(sum(LatencySpeeds)/numIterations)