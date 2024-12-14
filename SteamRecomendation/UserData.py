import SteamUser as SteamUser

API_KEY = "E895AD194456E34CA26E6270C5FE1C7B"
STEAM_ID = "76561198057456128"

class UserData:
    def __init__(self, name, genre, tags, playtime, appid, score):
        self.name = name
        self.genre = genre
        self.tags = tags
        self.playtime = playtime
        self.appid = appid
        self.score = score

steam_api = SteamUser.SteamUser(STEAM_ID, API_KEY)
owned_games = steam_api.get_owned_games(STEAM_ID)
recently_played = steam_api.get_recently_played_games(STEAM_ID)

def calculate_score(positive, negative):
    total_reviews = positive + negative
    if total_reviews == 0:
        return 0
    return positive / total_reviews

def collecting_game_data(game, data, time=""):
    game_time = game[time] / 60
    game_id = game["appid"]

    games_data = steam_api.get_games_data(game_id)

    game_positive = games_data["positive"]
    game_negative = games_data["negative"]

    game_score = calculate_score(game_positive, game_negative)
    score_scaled = (game_score * 10)

    name = games_data["name"]
    genre = games_data["genre"]

    if game_time <= 1:
        return

    if isinstance(games_data["tags"], dict):
        tags = list(games_data["tags"].keys())[:3]
    elif isinstance(games_data["tags"], list):
        tags = games_data["tags"][:3]
    else:
        tags = []


    data.append(UserData(
        name = name,
        genre = genre,
        tags = tags,
        playtime = game_time,
        appid = game_id,
        score = score_scaled,
    ))

user_game_data = []

iteration = 0

for game in owned_games:
    collecting_game_data(game, user_game_data, time="playtime_forever")

for game in user_game_data:
    break
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours, Game score: {game.score:.1f}")

recently_played_games = []

for game in recently_played:
    collecting_game_data(game, recently_played_games, time="playtime_2weeks")

for game in recently_played_games:
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours, Game score: {game.score:.1f}")


