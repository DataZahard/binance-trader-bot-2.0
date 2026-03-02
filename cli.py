import argparse
import sys
from bot.client import BinanceClient
from bot.logging_cfg import setup_logging
from rich.console import Console
from rich.table import Table

console = Console()
logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Professional Binance Futures Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], help="Required for standard")
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float, help="Price for LIMIT or TP")
    
    # OCO Arguments
    parser.add_argument("--oco", action="store_true", help="Place OCO (TP/SL) strategy")
    parser.add_argument("--stop_price", type=float, help="Required for OCO SL")

    args = parser.parse_args()
    
    try:
        bot = BinanceClient()

        if args.oco:
            if not args.price or not args.stop_price:
                raise ValueError("OCO requires --price (TP) and --stop_price (SL)")
            
            logger.info(f"Placing OCO: {args.side} {args.qty} {args.symbol} TP:{args.price} SL:{args.stop_price}")
            response = bot.place_oco_order(args.symbol, args.side, args.qty, args.price, args.stop_price)
            console.print(f"[bold green]OCO Placed![/bold green] TP ID: {response['tp']['orderId']}, SL ID: {response['sl']['orderId']}")
            
        else:
            if not args.type:
                raise ValueError("--type is required for standard orders.")
                
            logger.info(f"Placing {args.type}: {args.side} {args.qty} {args.symbol}")
            response = bot.place_order(args.symbol, args.side, args.type, args.qty, args.price)
            
            # Formatted Output
            table = Table(title="Order Success")
            table.add_column("Key", style="cyan")
            table.add_column("Value", style="magenta")
            table.add_row("Order ID", str(response.get("orderId")))
            table.add_row("Status", response.get("status"))
            table.add_row("Avg Price", response.get("avgPrice", "N/A"))
            console.print(table)

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        console.print(f"[bold red]Validation Error:[/bold red] {ve}")
    except Exception as e:
        logger.error(f"API Error: {e}")
        console.print(f"[bold red]API Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
