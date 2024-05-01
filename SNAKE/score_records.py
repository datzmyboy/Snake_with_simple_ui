import json

def create_player_json(player_name):
    try:
        # Attempt to read the existing player data from the file
        with open("players.json", "r") as file:
            players = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, initialize players as an empty list
        players = []

    # Check if the player already exists
    for player in players:
        if player["player_name"] == player_name:
            print("Player already exists.")
            return False

    # Create new player data
    player_data = {
        "player_name": player_name,
        "player_score": 0,  # Initialize player score to 0
    }

    # Append the new player data to the list of players
    players.append(player_data)

    # Write the updated player data back to the file
    with open("players.json", "w") as file:
        json.dump(players, file, indent=4)

    print("Player created successfully.")
    return True
def read_players():
    try:
        with open("players.json", "r") as file:
            try:
                players = json.load(file)
                if not players:
                    print("The file is empty.")
                return players
            except json.decoder.JSONDecodeError:
                print("The file is empty or does not contain valid JSON data.")
                return []
    except FileNotFoundError:
        return []

# Example usage:
def delete_player(player_name):
    players = read_players()
    players_count = len(players)
    new_set_of_players = []
    for player in players:
        if player["player_name"] != player_name:
            new_set_of_players.append(player)
    if len(new_set_of_players) < players_count:
        print("deleted")
    else:
         print("not deleted")
    with open("players.json", "w") as file:
        json.dump(new_set_of_players, file, indent=4)

def update_player(player_name, new_player_score):
    players = read_players()
    player_found = False  # Flag to track if player was found
    for player in players:
        if player["player_name"] == player_name:
            player["player_score"] = new_player_score
            player_found = True
            break  # No need to continue iterating if player is found

    if not player_found:
        print("Player not found.")

    with open("players.json", "w") as file:
        json.dump(players, file, indent=4)





# create_player_json("USER_DATA")
# user = read_players()
# myuser = user[0]
#
# score = myuser["player_score"]
# print(score)

