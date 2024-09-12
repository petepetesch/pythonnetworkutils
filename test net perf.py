import subprocess
import re

def ping(host):
    # Use the ping command
    process = subprocess.Popen(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error pinging {host}: {stderr.decode()}")
        return

    # Extract the average response time from the ping output
    match = re.search(r'avg = ([\d.]+) ms', stdout.decode())
    if match:
        avg_response_time = float(match.group(1))
        print(f"Average response time to {host}: {avg_response_time} ms")
    else:
        print("Could not determine average response time.")

if __name__ == "__main__":
    host = "google.com"
    ping(host)
