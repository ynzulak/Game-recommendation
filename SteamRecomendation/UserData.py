import SteamData as SteamData
import json
import statistics
import pandas as pd
import concurrent.futures
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

API_KEY = "E895AD194456E34CA26E6270C5FE1C7B"
STEAM_ID = "76561198969793537"

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

# ///////////////////////////////////////////////////////////////////

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

# Make vectorizer coisne similarity

game_names = [game["name"] for game in all_games_data]
tag_strings = [" ".join([f"{tag} " * count for tag, count in game["tags"].items()]) for game in all_games_data]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(tag_strings)

similarity_matrix = cosine_similarity(tfidf_matrix)
df_sim = pd.DataFrame(similarity_matrix, index=game_names, columns=game_names)


def recommend_games(game_name, df_sim, top_n=5):

    if game_name not in df_sim.index:
        return f"Game '{game_name}' not found in data."
    else:
        print(f"{game_name} is similar to:")

    similar_games = df_sim[game_name].sort_values(ascending=False)

    recommended_games = similar_games.iloc[1:top_n+1]

    return recommended_games

print("Based on your recently played games:")

# for game in recently_played:
#     game_name = game["name"]
#     recommendations = recommend_games(game_name, df_sim, top_n=5)

#     if isinstance(recommendations, str):
#         print(recommendations)
#     else:
#         for recommended_game in recommendations.index:
#             print(f" • {recommended_game}")
#         print("-" * 60)
        
game_count = 0
for game in owned_games:
    
    if game["playtime_forever"] / 60 >= median_playtime:
        game_count += 1
        game_name = game["name"]
        recommendations = recommend_games(game_name, df_sim, top_n=5)

        if isinstance(recommendations, str):
            print(recommendations)
        else:
            for recommended_game in recommendations.index:
                print(f" • {recommended_game}")
            print("-" * 60)
            
# def recommend_games_from_recent(recently_played, df_sim, top_n=10):
#     played_names = [game["name"] for game in recently_played if game["name"] in df_sim.index]

#     if not played_names:
#         return "None of the recently played games are in the similarity matrix."

#     combined_sim = df_sim.loc[played_names].sum()

#     combined_sim = combined_sim.drop(labels=played_names, errors="ignore")

#     recommended_games = combined_sim.sort_values(ascending=False).head(top_n)

#     return recommended_games

# recommendations = recommend_games_from_recent(recently_played, df_sim, top_n=10)
# print(recommendations)














