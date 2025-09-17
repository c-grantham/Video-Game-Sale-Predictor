# This code uses the id of a selected game and searches
# the ITAD API for its logged price history over time.
import requests
import csv
import pandas as pd

API_KEY = '2fbb4cb3aae1caa30275508a159b768f0631a9ab'
headers = {"User-Agent": "GamePriceIQ/1.0"}
date_format = '%Y-%m-%d'

# Function to retrieve the price history for a game
def get_price_history(id):
    # Send request to API using key and game's ID
    response = requests.get("https://api.isthereanydeal.com/games/history/v2", params={
        "key": API_KEY,
        "id": id
    }, headers=headers)
    # If failure, return
    if response.status_code != 200:
        print("Failed to retrieve price history.")
        return []
    print(response.status_code)

    # Convert API JSON response into a Python list
    data = response.json()

    # Storage list for data we want
    extract_data = []
    # For every price record entry retrieved for a game...
    for entry in data:
        try:
            # Try to extract the relevant information from sublists
            timestamp = entry['timestamp']
            date_time = pd.to_datetime(timestamp).tz_convert("UTC").tz_localize(None)
            date = date_time.date()
            year = date.year
            month = date.month
            day = date.day
            
            time = date_time.time()
            hour = time.hour
            minute = time.minute
            second = time.second
            shop = entry['shop']['name']
            deal = entry['deal']
            if deal is None:
                continue
            price = deal['price']['amount']
            regular = deal['regular']['amount']
            cut = deal['cut']
            # Append each extracted entry info to the list as a new tuple
            extract_data.append([date, time, year, month, day, hour, minute, second, price, regular, cut, shop])
        # Exception for missing fields or incorrect types to skip entry
        except(KeyError, TypeError) as e:
            print(f"Skipping malformed entry:{e}")
            continue
    
    df = pd.DataFrame(extract_data, columns=['date', 'time', 'year', 'month', 'day', 'hour', 'minute', 'second', 'price', 'regular', 'cut', 'shop'])
    
    # Returns raw data if further inspection required
    return df    