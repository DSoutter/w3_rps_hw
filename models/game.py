class Game():
    def __init__(self):
        pass

    def game_on(player1, player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock" and player2.choice == "scissors":
            return player1.name
        elif player1.choice == "paper" and player2.choice == "scissors":
            return player1.name
        elif player1.choice == "scissors" and player2.choice == "paper":
            return player1.name
        else:
            return player2.name
