from SteamRecommendation.recommendation_types.all_library_based import all_library_test
from SteamRecommendation.recommendation_types.per_game_based import per_game_recommendation
from SteamRecommendation.recommendation_types.recently_played_based import recently_played_recommendation

def main():
    while True:
        print("Choose, what type of recomendation do you have to see:")
        print("1. Based on you whole library")
        print("2. Based on your recently played games")
        print("3. Based on you whole library per game")
        print("4. Exit")

        choice = input("Your choice (1/2/3/4): ")

        if choice == "1":
            all_library_test()
        elif choice == "2":
            recently_played_recommendation()
        elif choice == "3":
            per_game_recommendation()
        elif choice == "4":
              print("Exiting the program.")
              break
        else:
            print("Incorrect choice, please try again.")

        continue_choice = input("Do you want to choose another option? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
    