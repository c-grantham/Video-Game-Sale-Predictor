# This code searches the ITAD API for games matching 
# a provided query. It returns a list of those games.
import requests

API_KEY = '2fbb4cb3aae1caa30275508a159b768f0631a9ab'
headers = {"User-Agent": "GamePriceIQ/1.0"}

# Function that looks up a game title and returns its info
def get_titles(game_title):
    # Send GET request to API using key and title for access and search
    response = requests.get(
        "https://api.isthereanydeal.com/games/search/v1", 
        params={
            "key": API_KEY,     
            "title": game_title
        }, headers=headers)
    # If request is successful...
    if response.status_code == 200:
        print(f"Game Info Status: {response.status_code}")
        # Return a *list*, converted from JSON
        return response.json()
    else:
        print("Failed to retrieve search.")
        return []