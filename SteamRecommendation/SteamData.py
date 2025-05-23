import requests

BASE_URL = "http://api.steampowered.com/"
USER_URL = BASE_URL + "ISteamUser/GetPlayerSummaries/v0002/"
GAME_URL = BASE_URL + "IPlayerService/GetOwnedGames/v0001/"
RECENTLY_PLAYED_URL = BASE_URL + "IPlayerService/GetRecentlyPlayedGames/v0001"
GAME_DATA_BASE_URL = "https://steamspy.com/api.php?request=appdetails&appid="

class SteamUser:
    def __init__(self, steam_id, api_key):
        self.steam_id = steam_id
        self.api_key = api_key
        
    def make_requests(self, url, params):
        response = requests.get(url, params=params)
        data = response.json()
        
        try:
            response
            data
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []

    def get_owned_games(self, steam_id):
        url = GAME_URL
        params = {
            "key": self.api_key,
            "steamid": steam_id,
            "format": "json",
            "include_appinfo": True, 
            "include_played_free_games": True 
        }

        data = self.make_requests(url, params)
        return data["response"]["games"] if data else []
    
    def get_recently_played_games(self, steam_id):
        url = RECENTLY_PLAYED_URL
        params = {
            "key": self.api_key,
            "steamid": steam_id,
            "format": "json", 
        }

        data = self.make_requests(url, params)
        return data["response"]["games"] if data else []
    
    def get_games_data(self, app_id):
        url = f"{GAME_DATA_BASE_URL}{app_id}"
        params = {}
        data = self.make_requests(url, params)
        return data