from SteamRecommendation.UserData import recently_played
from SteamRecommendation.game_recommendation_print import game_recommendation_print

def recently_played_recommendation():
    for game in recently_played:
        game_recommendation_print(game)