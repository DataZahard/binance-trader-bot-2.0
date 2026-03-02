import re

def validate_symbol(symbol: str) -> bool:
    """Checks if symbol follows Binance format (e.g., BTCUSDT)."""
    pattern = r"^[A-Z0-9]{5,12}$"
    if not re.match(pattern, symbol.upper()):
        raise ValueError(f"Invalid symbol format: {symbol}. Expected format like 'BTCUSDT'")
    return True

def validate_quantity(quantity: float) -> bool:
    """Ensures quantity is a positive number."""
    if quantity <= 0:
        raise ValueError(f"Quantity must be positive. Received: {quantity}")
    return True

def validate_price(price: float) -> bool:
    """Ensures price is a positive number."""
    if price is not None and price <= 0:
        raise ValueError(f"Price must be positive. Received: {price}")
    return True
