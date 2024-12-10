import SteamUser as SteamUser

API_KEY = "E895AD194456E34CA26E6270C5FE1C7B"
STEAM_ID = "76561198057456128"

class UserData:
    def __init__(self, name, genre, tags, playtime, appid):
        self.name = name
        self.genre = genre
        self.tags = tags
        self.playtime = playtime
        self.appid = appid

steam_api = SteamUser.SteamUser(STEAM_ID, API_KEY)
owned_games = steam_api.get_owned_games(STEAM_ID)
recently_played = steam_api.get_recently_played_games(STEAM_ID)

game_times = []
user_game_data = []

iteration = 0

#Looping through Steam account to display games
for game in owned_games:
    game_time = game["playtime_forever"] / 60
    game_id = game["appid"]

    games_data = steam_api.get_games_data(game_id)

    name = games_data["name"]
    genre = games_data["genre"]

    if game_time <= 1:  
        continue
    game_times.append(game_time)

    iteration += 1  

    if isinstance(games_data["tags"], dict):
        tags = list(games_data["tags"].keys())[:3]
    elif isinstance(games_data["tags"], list):
        tags = games_data["tags"][:3]
    else:
        tags = []


    user_game_data.append(UserData(
        name = name,
        genre = genre,
        tags = tags,
        playtime = game_time,
        appid = game_id
    ))

for game in user_game_data:
    break
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours")

total_time = sum(game_times)
print(f"All time spent on games: {total_time:.1f}")

recently_game_times = []
recently_played_games = []

for game in recently_played:
    game_time = game["playtime_2weeks"] / 60
    game_id = game["appid"]

    games_data = steam_api.get_games_data(game_id)

    name = games_data["name"]
    genre = games_data["genre"]

    if game_time <= 1:  
        continue
    
    recently_game_times.append(game_time)

    iteration += 1  

    if isinstance(games_data["tags"], dict):
        tags = list(games_data["tags"].keys())[:3]
    elif isinstance(games_data["tags"], list):
        tags = games_data["tags"][:3]
    else:
        tags = []


    recently_played_games.append(UserData(
        name = name,
        genre = genre,
        tags = tags,
        playtime = game_time,
        appid = game_id
    ))


for game in recently_played_games:
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours")

recently_total_time = sum(recently_game_times)
print(f"All time spent on games: {recently_total_time:.1f}")
