import random
options = ["rock", "paper", "scissors"]
playagain=True
while playagain:
    game = input(""""
    ---------------------------------
    |   Rock, Paper, Scissors Game  |
    ---------------------------------
    |   1. Rock                     |
    |   2. Paper                    |
    |   3. Scissors                 |
    |   4. Quit                     |
    ---------------------------------
    """)
    if game == "1":
        player_choice = "rock"
    elif game == "2":
        player_choice = "paper"
    elif game == "3":
        player_choice = "scissors"      
    elif game == "4":
        quit()
    else:
        print("Invalid input. Please try again.")
        playagain = input("Do you want to play again? (y/n) ")
        continue
    computer_choice = random.choice(options)
    print("You chose " + player_choice + ", and the computer chose " + computer_choice + ".")

    if player_choice == computer_choice:
        print("You drew. Play again.")
    elif player_choice == "rock" and computer_choice == "scissors":  # rock beats scissorsa
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":  # paper beats rock           
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":  # scissors beats paper   
        print("You win!")
    else:  # computer wins
        print("Computer wins.")
    playagain = input("Do you want to play again? (y/n) ")
    if playagain == "y":
        playagain = True
    else:
        playagain = False
        print("Thanks for playing!")    
        SystemExit()
            