import time
import os
import sys
from dotenv import load_dotenv
from tracker.tracker import get_system_info, get_cpu_temp, get_cpu_usage, get_ram_usage, send_data_to_influxdb

# Load environment variables from .env file
load_dotenv()

# Retrieve interval from environment variables
try:
    interval = int(os.getenv('INTERVAL', 60))
except ValueError:
    interval = 60
    print("INTERVAL environment variable is not a valid integer. Using default value of 60 seconds.")

if __name__ == "__main__":
    hostname, ip_address = get_system_info()
    
    while True:
        try:
            # Collect system metrics
            cpu_temp = get_cpu_temp()
            cpu_usage = get_cpu_usage()
            ram_usage = get_ram_usage()
            
            # Print collected metrics
            print(f"Host: {hostname} ({ip_address}) - CPU Temp: {cpu_temp} °C, CPU Usage: {cpu_usage} %, RAM Usage: {ram_usage} %")
            
            # Send metrics to InfluxDB
            send_data_to_influxdb(hostname, ip_address, cpu_temp, cpu_usage, ram_usage)
        
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

        time.sleep(interval)
