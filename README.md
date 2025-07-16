## Server Status Checker

This Python script connects to multiple remote Windows servers using **WinRM** and runs a PowerShell script to collect system health metrics. The goal is to quickly check system health without logging into each machine individually.

## Script Process

- Connects to a list of Windows servers over the network
- Gathers the following system information:
  - Memory usage
  - CPU load
  - Disk usage (Drive C)
  - System uptime
- Returns a simple status report per server, with alerts for high usage

## System Requirements

- Python 3.8+
- [`pipenv`](https://pipenv.pypa.io/en/latest/)
- Remote Windows servers with:
  - WinRM enabled
  - PowerShell installed
  - Network access from your machine

## Script Execution Process

1. Clone or download this repository
2. Set up the environment:
   ```bash
   pipenv install
   pipenv shell
   ```
3. Update the server list in main.py or read from servers.csv
4. Run the script:
   ```
   python -m src.main
   ```
5. Exit pipenv
   ```
   exit
   ```
