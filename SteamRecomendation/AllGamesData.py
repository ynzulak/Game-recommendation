# This code fetches game data from the SteamSpy API and saves it to a JSON file. It includes all needed data to use in code.

import requests
import json

GAME_DATA_BASE_URL = "https://steamspy.com/api.php?request="
GAME_DATA_APP_ID = f"appdetails&appid="

def make_requests(url, params):
    response = requests.get(url, params=params)
    data = response.json()
        
    try:
        response
        data
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def get_games_data_by_id(app_id):
    url = f"{GAME_DATA_BASE_URL}{GAME_DATA_APP_ID}{app_id}"
    params = {}
    data = make_requests(url, params)
    return data
    
def get_games_data():
    all_data = {}
    url = f"{GAME_DATA_BASE_URL}all"
    params = {}
    data = make_requests(url, params)
    if isinstance(data, dict):
            all_data.update(data)
        
    return all_data

all_games_data = get_games_data()

all_games_data_list = []

for game in all_games_data.values():
    appid = game["appid"]
    game_data = get_games_data_by_id(appid) 
    all_games_data_list.append(game_data) 


with open("games_data.json", "w", encoding="utf-8") as file:
    json.dump(all_games_data_list, file, ensure_ascii=False, indent=4)






