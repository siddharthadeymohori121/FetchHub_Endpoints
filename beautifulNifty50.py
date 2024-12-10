import requests
import pandas as pd

# Function to fetch Nifty50 stock list
def fetch_nifty50_list():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)  # Fetch cookies
    response = session.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    stocks = data["data"]
    
    # Debug step
    print(stocks[0].keys())  # Print the available keys in the response
    
    # Adjust DataFrame creation based on available columns
    df = pd.DataFrame(stocks)
    required_columns = ['symbol', 'dayHigh', 'dayLow', 'lastPrice', 'change', 'pChange']
    df = df[required_columns]
    df.columns = ['Symbol', 'Day High', 'Day Low', 'Last Price', 'Change', 'PChange']
    return df

# Fetch and print Nifty50 data
def fetch_and_print_nifty50_data():
    try:
        print("Fetching Nifty50 stock list...")
        nifty50_df = fetch_nifty50_list()
        
        # Print the DataFrame
        print(nifty50_df)
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to fetch and print Nifty50 data
fetch_and_print_nifty50_data()