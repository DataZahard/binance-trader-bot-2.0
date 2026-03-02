# Binance Futures Trader Bot v2.0

A professional, modular Python trading application designed for the **Binance Futures Testnet (USDT-M)**. This bot is engineered for reliability, secure credential management, and robust error handling, making it a solid foundational tool for automated trading strategies.



## Features
* **Order Types**: Supports Market, Limit, and OCO (One-Cancels-the-Other / Take Profit & Stop Loss) strategies.
* **Input Validation**: Strict validation for symbols, quantities, and prices *before* API calls are made to prevent invalid requests.
* **Security**: API credentials are kept separate via `.env` files, following best practices for secure development.
* **Detailed Logging**: Comprehensive log tracking for all API interactions, errors, and validation checks stored in `logs/trading.log`.
* **Mobile Optimized**: Engineered to run smoothly on Android/iOS via **Termux**.

## Setup & Installation

### 1. Prerequisites
Ensure you have Python 3 installed. If using Termux:
```bash
pkg update && pkg upgrade -y
pkg install python rust binutils -y
```

### 2. Clone the Repository
```bash
git clone https://github.com/datazahard/binance-trader-bot-2.0.git
cd binance-trader-bot-2.0
```

### 3. Install Dependencies
Set up a virtual environment and install the required libraries:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configuration
Create your environment file from the template and add your Testnet API credentials:
```bash
cp .env.example .env
nano .env
```

Add your BINANCE_API_KEY and BINANCE_API_SECRET inside the .env file.

### ​5. Permissions (Termux/Linux)
```bash
chmod +x cli.py
```

## Usage Examples

| Order Type | Command | Example |
| :--- | :--- | :--- |
| Market | `python cli.py` | `--symbol BTCUSDT --side BUY --type MARKET --qty 0.001` |
| Limit | `python cli.py` | `--symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 60000` |
| OCO | `python cli.py` | `--symbol BTCUSDT --side BUY --qty 0.001 --oco --price 70000 --stop_price 55000` |

## Understanding Logs

All actions, successes, and errors are recorded in logs/trading.log.

* **INFO**: Normal operation (placing orders, validation success).
* **ERROR**: API issues, invalid inputs (e.g., negative quantity, wrong symbol format), or network failures.

To monitor activity in real-time, use:
```bash
tail -f logs/trading.log
```
## Example Logs
Below is an example of what `logs/trading.log` looks like after executing various commands:

```text
2026-03-02 10:00:01,123 - TradingBot - INFO - Placing LIMIT: BUY 0.001 BTCUSDT
2026-03-02 10:00:01,850 - TradingBot - INFO - Order Success: 1000001
2026-03-02 10:05:10,555 - TradingBot - INFO - Placing OCO: SELL 0.005 BTCUSDT TP:75000 SL:50000
2026-03-02 10:05:11,200 - TradingBot - INFO - Order Success: 1000002
2026-03-02 10:05:11,750 - TradingBot - INFO - Order Success: 1000003
2026-03-02 10:10:00,001 - TradingBot - ERROR - Validation Error: Quantity must be positive. Received: -0.1


### Developed by DataZahard
