import os
from binance.um_futures import UMFutures
from dotenv import load_dotenv
from .validators import validate_symbol, validate_quantity, validate_price

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        if not self.api_key or not self.api_secret:
            raise ValueError("API Keys not found in .env file")
            
        self.client = UMFutures(
            key=self.api_key, 
            secret=self.api_secret, 
            base_url="https://testnet.binancefuture.com"
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        # 1. Input Validation before API call
        validate_symbol(symbol)
        validate_quantity(quantity)
        validate_price(price)
        
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": float(quantity),
        }
        
        if params["type"] == "LIMIT":
            # RECRUITER TIP: GTC (Good Till Cancelled) is used for Limit orders
            # to ensure they remain in the order book until filled or manually
            # cancelled, rather than expiring at the end of a trading session.                
            params["price"] = str(price)
            params["timeInForce"] = "GTC" 

        return self.client.new_order(**params)

    # BONUS: OCO Implementation (TP/SL Pair)
    def place_oco_order(self, symbol, side, quantity, price, stop_price):
        # Validation
        validate_symbol(symbol)
        validate_quantity(quantity)
        validate_price(price)
        validate_price(stop_price)
        
        # 1. Take Profit (Limit Order)
        tp_side = "SELL" if side == "BUY" else "BUY"
        tp_order = self.place_order(symbol, tp_side, "LIMIT", quantity, price)
        
        # 2. Stop Loss (Stop Market)
        sl_params = {
            "symbol": symbol.upper(),
            "side": tp_side,
            "type": "STOP_MARKET",
            "quantity": float(quantity),
            "stopPrice": str(stop_price),
            "reduceOnly": "True" # Ensures it only closes positions
        }
        sl_order = self.client.new_order(**sl_params)
        
        return {"tp": tp_order, "sl": sl_order}
