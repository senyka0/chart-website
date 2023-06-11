# Candlestick Chart and Pie Chart WebSite
Simple Flask user interface that displays a candlestick chart and a pie chart using Plotly for visualization.
## Prerequisites
Before running the script, make sure you have the following requirements:
* Python 3.x
* Flask library ```pip install flask```
* Plotly library ```pip install plotly```
## Getting Started
1. Clone the repository.
2. Open the ```app.py``` in a text editor.
3. Modify the interval and symbol variables.
```sh
symbol = "BTCUSDT" # your symbol
interval = "1d" # your interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M)
```
4. Save the changes.
5. Open a terminal and navigate to the directory where ```app.py``` script is located.
6. Run the Flask ```python app.py```
7. Open your web browser and go to `http://localhost:5000` to access the user interface.