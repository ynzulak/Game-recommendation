import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




with open('./games_data.json', 'r', encoding="utf-8") as file:
    all_games_data = json.load(file)

def cosine_similarity_build():

    game_names = [game["name"] for game in all_games_data]
    tag_strings = [" ".join([f"{tag} " * count for tag, count in game["tags"].items()]) for game in all_games_data]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(tag_strings)

    similarity_matrix = cosine_similarity(tfidf_matrix)
    df_sim = pd.DataFrame(similarity_matrix, index=game_names, columns=game_names)

    return df_sim

