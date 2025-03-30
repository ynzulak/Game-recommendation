import SteamData as SteamData
import json
import pandas as pd
import concurrent.futures
from sklearn.feature_extraction.text import TfidfVectorizer

API_KEY = "E895AD194456E34CA26E6270C5FE1C7B"
STEAM_ID = "76561198057456128"

# Getting data from game_data file

with open('./games_data.json', 'r', encoding="utf-8") as file:
    all_games_data = json.load(file)


steam_api = SteamData.SteamUser(STEAM_ID, API_KEY)
owned_games = steam_api.get_owned_games(STEAM_ID)
recently_played = steam_api.get_recently_played_games(STEAM_ID)

# Fetching data from Steampy for games in your library (like tags, genre, etc.)

def fetch_game_data(app_id):
    return steam_api.get_games_data(app_id)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_game_data, [game["appid"] for game in owned_games])


owned_games_data = list(results)


# Make coisne similarity
for game in owned_games_data:
    game.pop("languages")
    for owned_game in owned_games:
        if game['appid'] == owned_game['appid']:
            game["playtime_forever"] = owned_game['playtime_forever']


print(owned_games_data[0], owned_games_data[1])



def calculate_score(positive, negative):
    total_reviews = positive + negative
    if total_reviews == 0:
        return 0
    return positive / total_reviews


for game in owned_games_data:
    break
    score = calculate_score(game["positive"], game["negative"])
    game_time = game["playtime_forever"] / 60
    print(f"{game["name"]}, Time spent: {game_time:.1f} hours, tags: {game["tags"]}, score: {score}")












