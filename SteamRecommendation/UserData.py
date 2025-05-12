from SteamRecommendation.SteamData import SteamUser
import json
import concurrent.futures as conc

import statistics
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from SteamRecommendation.steam_id import extract_steam_id

steam_id = extract_steam_id()

API_KEY = "E895AD194456E34CA26E6270C5FE1C7B"
STEAM_ID = steam_id

# Getting data from game_data file
with open('./games_data.json', 'r', encoding="utf-8") as file:
    all_games_data = json.load(file)
    
steam_api = SteamUser(STEAM_ID, API_KEY)
owned_games = steam_api.get_owned_games(STEAM_ID)
recently_played = steam_api.get_recently_played_games(STEAM_ID)

# Fetching data from Steampy for games in your library (like tags, genre, etc.)
def fetch_game_data(app_id):
    return steam_api.get_games_data(app_id)

with conc.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_game_data, [game["appid"] for game in owned_games])


owned_games_data = list(results)

for game in owned_games_data:
    game.pop("languages")
    for owned_game in owned_games:
        if game['appid'] == owned_game['appid']:
            game["playtime_forever"] = owned_game['playtime_forever']


def get_unique_tags(game_gata):
    unique_tags = set()
    for tags in all_games_data:
        unique_tags.update(tags["tags"].keys())

    return sorted(unique_tags)  

def calculate_score(positive, negative):
    total_reviews = positive + negative
    if total_reviews < 100:
        return 0
    return (positive / total_reviews) * 100 


total_playtime = []
for game_time in owned_games_data:
    time = game_time["playtime_forever"] / 60
    total_playtime.append(time)
    median_playtime = statistics.median(total_playtime)


for game in owned_games_data:
    break
    score = calculate_score(game["positive"], game["negative"])
    game_time = game["playtime_forever"] / 60
    print(f"{game["name"]}, Time spent: {game_time:.1f} hours, score: {score}")















