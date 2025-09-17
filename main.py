import requests
import csv
from searchgames import get_titles
from pricehistory import get_price_history
from dataloader import load_data

API_KEY = '2fbb4cb3aae1caa30275508a159b768f0631a9ab'
headers = {"User-Agent": "GamePriceIQ/1.0"}

title = input()
games = get_titles(title)

if games:
    for game in games:
        print(f"{game['title']}: {game['id']}")
    select = games[0]
    pricing = get_price_history(select['id'])
    print((pricing))
    load_data(pricing)
else: print("No games found.")



