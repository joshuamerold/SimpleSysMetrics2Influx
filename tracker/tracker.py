import psutil
import requests
import platform
import socket
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve InfluxDB configuration from environment variables
influxdb_url = os.getenv('INFLUXDB_URL')
influxdb_user = os.getenv('INFLUXDB_USER')
influxdb_password = os.getenv('INFLUXDB_PASSWORD')

# Get CPU temperature (Linux only)
def get_cpu_temp():
    try:
        if platform.system() == 'Linux':
            temp = psutil.sensors_temperatures().get('coretemp', [])[0].current
        elif platform.system() == 'Windows':
            temp = 0
        return temp
    except:
        return None

# Get CPU usage percentage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Get RAM usage percentage
def get_ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent

# Get system hostname and IP address
def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

# Send collected metrics to InfluxDB
def send_data_to_influxdb(hostname, ip_address, cpu_temp, cpu_usage, ram_usage):
    data = f"system_metrics,host={hostname},ip={ip_address} cpu_temp={cpu_temp},cpu_usage={cpu_usage},ram_usage={ram_usage}"
    
    try:
        response = requests.post(
            influxdb_url,
            auth=(influxdb_user, influxdb_password),
            data=data
        )
        
        if response.status_code == 204:
            print("Daten erfolgreich an InfluxDB gesendet.")
        else:
            print(f"Fehler beim Senden an InfluxDB: {response.status_code}, {response.text}")
            
    except Exception as e:
        print(f"Fehler: {e}")