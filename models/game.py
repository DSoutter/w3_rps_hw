class Game():
    def __init__(self):
        pass

    def game_on(player1, player2):
        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock" and player2.choice == "scissors":
            return f"{player1.name} wins by playing rock"
        elif player1.choice == "paper" and player2.choice == "scissors":
            return f"{player1.name} wins by playing paper"
        elif player1.choice == "scissors" and player2.choice == "paper":
            return f"{player1.name} wins by playing scissors"
        else:
            return f"{player2.name} wins by playing {player2.choice}"
