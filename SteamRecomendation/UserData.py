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
all_games_data = steam_api.get_games_data()

def calculate_score(positive, negative):
    total_reviews = positive + negative
    if total_reviews == 0:
        return 0
    return positive / total_reviews



# def collecting_all_game_data(game, game_data_dict):
#     game_id = game["appid"]

#     if game_id not in game_data_dict:
#         return 

#     game_data = game_data_dict[game_id]

#     game_positive = game_data["positive"]
#     game_negative = game_data["negative"]

#     game_score = calculate_score(game_positive, game_negative)
#     score_scaled = (game_score * 10)

#     name = game_data["name"]
#     genre = game_data["genre"]

#     if isinstance(game_data["tags"], dict):
#         tags = list(game_data["tags"].keys())[:3]
#     elif isinstance(game_data["tags"], list):
#         tags = game_data["tags"][:3]
#     else:
#         tags = []


#     return {
#     "name": name,
#     "genre": genre,
#     "tags": tags,
#     "appid": game_id,
#     "score": score_scaled,
# } chyba nie bede tego potrzebowal (sprawdzic to) ============================

from collections import Counter
all_game_data = []
game_list = list(all_games_data.values())

# for game in game_list:
#     collecting_all_game_data(game, all_game_data)
# print("=====d=d=sd=as=d=as=das=d=asd=asd")
# print(game_list)
all_genres = [game['genre'] for game in all_game_data]


all_tags = []
for game in all_game_data:
    all_tags.extend(game['tags']) 


genre_counts = Counter(all_genres)  
tag_counts = Counter(all_tags)     

print("Unikalne gatunki i ich liczby:")
for genre, count in genre_counts.items():
    print(f"{genre}: {count}")

print("\nUnikalne tagi i ich liczby:")
for tag, count in tag_counts.items():
    print(f"{tag}: {count}")


def collecting_game_data(game, data, game_data_dict, time=""):
    game_time = game[time] / 60 
    game_id = game["appid"]
    
    if game_id not in game_data_dict:
        return 

    game_data = game_data_dict[game_id]
    game_positive = game_data["positive"]
    game_negative = game_data["negative"]
    
    game_score = calculate_score(game_positive, game_negative)
    score_scaled = (game_score * 10)
    
    name = game_data["name"]

    genre = game_data.get("genre", "Unknown")

    if "tags" not in game_data:
        tags = []
    elif isinstance(game_data["tags"], dict):
        tags = list(game_data["tags"].keys())[:3] 
    elif isinstance(game_data["tags"], list):
        tags = game_data["tags"][:3]  
    else:
        tags = []

    if game_time <= 1: 
        return

    data.append(UserData(
        name=name,
        genre=genre,
        tags=tags,
        playtime=game_time,
        appid=game_id,
        score=score_scaled,
    ))


game_data_dict = {game["appid"]: game for game in all_games_data.values()}
user_game_data = []

for game in owned_games:
    collecting_game_data(game, user_game_data, game_data_dict, time="playtime_forever")

for game in user_game_data:
    break
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours, Game score: {game.score:.1f}")
""
print("========================================================")


recently_played_games = []

for game in recently_played:
    collecting_game_data(game, recently_played_games, game_data_dict, time="playtime_2weeks")

for game in recently_played_games:
    break    
    print(f"{game.name}: Genre: {game.genre}, Tags: {', '.join(game.tags)}, Time spent: {game.playtime:.1f} hours, Game score: {game.score:.1f}")
    

for game in all_games_data.values():
    print(game["name"])







