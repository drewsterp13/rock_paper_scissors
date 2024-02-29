import entity, time

computer = entity.Computer()
player = entity.Player()

class Command():
    # This begins the game
    def beginGame(self):
        print("Welcome to the game of Rock, Paper, n Scissors")
        print("where you choose one of the three objects and the computer chooses it as well.")
        print("Some items are stronger than others and the one with the strongest item wins!")
        print()
        time.sleep(2)
    
    # This plays the game
    def runGame(self, continue_game):
        computer_action = computer.randomAction()
        player_action = player.chooseAction()
        continue_game = player.compareAction(player_action, computer_action)
        return continue_game