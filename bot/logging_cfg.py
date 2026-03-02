import logging
import os

def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(leve>
        handlers=[
            logging.FileHandler("logs/trading.l>
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("TradingBot")
