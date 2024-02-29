import game

# NOTE: USE THIS FILE TO RUN THE PROGRAM

play_game = game.Command()

run_game = True

# This runs the game

while run_game:
    play_game.beginGame()
    run_game = play_game.runGame(run_game)
    if run_game == False:
        break
