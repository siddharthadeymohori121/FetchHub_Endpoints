import requests
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

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
    
    # Adjust DataFrame creation based on available columns
    df = pd.DataFrame(stocks)
    required_columns = ['symbol', 'dayHigh', 'dayLow', 'lastPrice', 'change', 'pChange']
    df = df[required_columns]
    df.columns = ['Symbol', 'Day High', 'Day Low', 'Last Price', 'Change', 'PChange']
    return df

# API endpoint to get the Nifty50 stock data
@app.route('/api/nifty50', methods=['GET'])
def get_nifty50_data():
    try:
        nifty50_df = fetch_nifty50_list()
        # Convert DataFrame to JSON format
        result = nifty50_df.to_dict(orient='records')
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)