class Game():
    def __init__(self):
        pass

    def game_on(player1, player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock" and player2.choice == "scissors":
            return player1
        elif player1.choice == "paper" and player2.choice == "rock":
            return player1
        elif player1.choice == "scissors" and player2.choice == "paper":
            return player1
        else:
            return player2
