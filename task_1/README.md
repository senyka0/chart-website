# Binance Data Collection
Script to collect data from the Binance API for a provided interval and symbol. 
The collected data is saved in CSV format.
## Prerequisites
Before running the script, make sure you have the following requirements:
* Python 3.x
* requests library ```pip install requests```
* pandas library ```pip install pandas```
## Getting Started
1. Clone the repository.
2. Open ``data_collection.py``` in a text editor.
3. Modify the interval and symbol variables.
```sh
symbol = "BTCUSDT" # your symbol
interval = "1d" # your interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)
```
4. Save the changes.
5. Open a terminal and navigate to the directory where ```data_collection.py``` script is located.
6. Run ```python data_collection.py``` to execute the script:
## To collect data at regular intervals
Using cron job on Linux server:
1. Open the terminal.
2. Type ```crontab -e``` to open the cron table for editing.
3. Add a new line for each interval you want to schedule, following the cron syntax.
4. For example, to run the script every day at 12:00 AM: ```0 0 * * * /usr/bin/python /path/to/data_collection.py```
5. Save the cron table and exit the editor.
6. The script will run automatically at the specified intervals.