from SNAKE.score_records import read_players
Window_WIDTH = 600
Window_Height = 600
player_score = 0
Snake_size = 20
Apple_size = 10

high = read_players()
the_user_data = high[0]

high_score = the_user_data["player_score"]