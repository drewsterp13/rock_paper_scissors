import random, time

# These classes are the different actions that the different entites can do, Both is what both entites can do, Computer is what only the computer can do, and Player is what only the player do
# In the game module, there should be two entites (objects), one is "player" and the other is "computer".

class Both():
    # This compares the actions of one another
    def compareAction(self, useract, cmpact):
        if useract.lower() == "i quit":
            print("Thank you for playing")
            return False
        else:
            print(f"You choose {useract.title()}")
            print(f"Computer choose {cmpact.title()}")
            print()
            time.sleep(1)
            if useract.title() == cmpact:
                print("Game Tied")
            elif useract.title() == "Rock":
                if cmpact.title() == "Paper":
                    print("You Lost :(")
                else:
                    print("You Win!")
            elif useract.title() == "Paper":
                if cmpact.title() == "Scissors":
                    print("You Lost :(")
                else:
                    print("You Win!")
            elif useract.title() == "Scissors":
                if cmpact.title() == "Rock":
                    print("You Lost :(")
                else:
                    print("You Win!")
            else:
                print("Invalid Word")
            print()
            time.sleep(1)
            return True
                
class Computer(Both):
    # This randomizes the action for the computer entity
    def randomAction(self):
        actions_list = ["Rock", "Paper", "Scissors"]
        chosen_action = random.randint(0, 2)
        return actions_list[chosen_action]
    
class Player(Both):
    # This lets the player choose the action
    def chooseAction(self):
        print("Choose your action")
        print('Enter "rock" for Rock')
        print('Enter "paper" for Paper')
        print('Enter "scissors" for Scissors')
        print('Enter "i quit" to end the game')
        chosen_action = input("ENTER HERE: ")
        print()
        return chosen_action