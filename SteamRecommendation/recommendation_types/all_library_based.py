from SteamRecommendation.CosineSimilarity import cosine_similarity_build
from SteamRecommendation.game_recommendation_print import game_recommendation_print
from SteamRecommendation.UserData import recently_played, owned_games, median_playtime


df_sim = cosine_similarity_build()
        

def all_library_recommendation(owned_games, df_sim, top_n=10):
    played_names = [game["name"] for game in owned_games if game["name"] in df_sim.index]

    if not played_names:
        return "None of the recently played games are in the similarity matrix."

    combined_sim = df_sim.loc[played_names].sum()
    combined_sim = combined_sim.drop(labels=played_names, errors="ignore")
    recommended_games = combined_sim.sort_values(ascending=False).head(top_n)

    print("Based on your recently played games:")
    for game in recommended_games.index:
        print(f" • {game}")

def all_library_test():
    all_library_recommendation(owned_games, df_sim, top_n=10)