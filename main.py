import sys
import argparse
from src.database import engine, Base
from src.tracker import add_product, track_prices

def init_db():
    """Initialize the database tables."""
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database ready.")

def main():
    parser = argparse.ArgumentParser(description="Professional Price Tracker CLI")
    
    # Define commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Command: init
    subparsers.add_parser("init", help="Initialize the database")
    
    # Command: add <url>
    add_parser = subparsers.add_parser("add", help="Add a new product to track")
    add_parser.add_argument("url", type=str, help="Product URL")
    add_parser.add_argument("--target", type=float, help="Target price (optional)", default=None)
    
    # Command: track
    subparsers.add_parser("track", help="Run the price tracker for all products")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_db()
    elif args.command == "add":
        print(f"Adding product: {args.url}")
        add_product(args.url, args.target)
    elif args.command == "track":
        print("Running price tracker...")
        track_prices()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()