import re

def extract_steam_id():
    print("Steam Game Recommendation System")
    url_or_id = input("Please Enter your SteamID (URL or ID): ")
    
    match = re.search(r"steamcommunity\.com/profiles/(\d+)", url_or_id)
    if match:
        steam_id = match.group(1)
        if len(steam_id) == 17:
            print("Steam ID:", steam_id)
            return steam_id
    
    if len(url_or_id) == 17 and url_or_id.isdigit():
        print("Steam ID:", url_or_id)
        return url_or_id
    
    print("Incorrect SteamID")
    return None
