new_game = "Yes"
while new_game == "Yes":
    player1move = input("Player 1, choose rock, paper or scissors: ")
    player2move = input("Player 2, choose rock, paper, or scissors: ")

# player1 picks rock
    if player1move == "rock" and player2move == "scissors":
        print("Player 1 wins!")
    elif player1move == "rock" and player2move == "paper":
        print("Player 2 wins!")
    elif player1move == "rock" and player2move == "rock":
        print("It's a draw!")

# player1 picks paper
    elif player1move == "paper" and player2move == "rock":
        print("Player 1 wins!")
    elif player1move == "paper" and player2move == "paper":
        print("It's a draw!")
    elif player1move == "paper" and player2move == "scissors":
        print("Player 2 wins!")

# player1 picks scissors
    elif player1move == "scissors" and player2move == "rock":
        print("Player 2 wins!")
    elif player1move == "scissors" and player2move == "paper":
        print("Player 1 wins!")
    elif player1move == "scissors" and player2move == "scissors":
        print("It's a draw!")
    else:
        "Invalid play(s)."
    new_game = input("Would you like to play a new game (Yes or No)? ")
print("Thanks for playing!")
