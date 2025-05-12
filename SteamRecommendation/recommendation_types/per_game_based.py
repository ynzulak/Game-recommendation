from SteamRecommendation.UserData import owned_games, median_playtime
from SteamRecommendation.game_recommendation_print import game_recommendation_print

def per_game_recommendation(): 
    for game in owned_games:
        if game["playtime_forever"] / 60 >= median_playtime:
            game_recommendation_print(game)