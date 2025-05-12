from SteamRecommendation.CosineSimilarity import cosine_similarity_build

df_sim = cosine_similarity_build()

def recommend_games(game_name, df_sim, top_n=5):

    if game_name not in df_sim.index:
        return f"Game '{game_name}' not found in data."
    else:
        print(f"{game_name} is similar to:")

    similar_games = df_sim[game_name].sort_values(ascending=False)

    recommended_games = similar_games.iloc[1:top_n+1]

    return recommended_games

def game_recommendation_print(game):
        game_name = game["name"]
        recommendations = recommend_games(game_name, df_sim, top_n=5)

        if isinstance(recommendations, str):
            print(recommendations)
        else:
            for recommended_game in recommendations.index:
                print(f" • {recommended_game}")
            print("-" * 60)

