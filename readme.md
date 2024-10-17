
# SimpleSysMetrics2Influx

SimpleSysMetrics2Influx is a lightweight tool designed for basic system metrics collection across multiple systems.
The primary goal of this project is functionality, not security. It is intended for internal use in a trusted network
environment, and **security features have not been implemented**.

## Features

- Collects CPU temperature, CPU load, and RAM usage from multiple servers.
- Sends the collected data, along with the hostname and IP address, to a database for easy monitoring and analysis.

## Requirements

- Python 3.x
- Required packages (see `requirements.txt`)

## Setup

1. Clone this repository:
    ```bash
    git clone <https://github.com/joshuamerold/SimpleSysMetrics2Influx.git>
    cd SimpleSysMetrics2Influx
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the `.env` file with your database connection details and (optional) intervall.
    ```env
    INFLUXDB_URL=http://<HOST>:8086/write?db=<DB_NAME>
    INFLUXDB_USER=<USER>
    INFLUXDB_PASSWORD=<PASSWORD>
    #INTERVAL=60 # default 60 seconds
    ```
4. Run the script:
    ```bash
    python main.py
    ```

## Note

This project is **not** designed with security in mind. It is a simple tool for data collection within a controlled and
trusted network environment. Please avoid using this in a publicly accessible or sensitive production environment.