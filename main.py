import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables from .env file
load_dotenv()

def main():
    api_key = os.getenv("APCA_API_KEY_ID")
    api_secret = os.getenv("APCA_API_SECRET_KEY")
    base_url = os.getenv("APCA_API_BASE_URL", "https://paper-api.alpaca.markets")

    if not api_key or not api_secret:
        print("Error: API Key or Secret Key not found. Please check your .env file.")
        return

    try:
        # Initialize the Alpaca API connection
        api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
        
        # Check account status
        account = api.get_account()
        
        print(f"Connection Successful!")
        print(f"Account ID: {account.id}")
        print(f"Status: {account.status}")
        print(f"Cash: ${account.cash}")
        print(f"Portfolio Value: ${account.portfolio_value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()