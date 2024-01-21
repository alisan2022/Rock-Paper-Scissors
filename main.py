import random

player_win_counter = 0
pc_win_counter = 0

def rock_paper_scissors(x):
    global player_win_counter
    global pc_win_counter

    scissors = "scissors"
    paper = "paper"
    rock = "rock"

    pc = random.choice([scissors, paper, rock])

    if x == scissors:
        if pc == rock:
            pc_win_counter += 1
            print("Pc wins!")
        elif pc == paper:
            player_win_counter += 1
            print("You win!")
        else:
            print("Draw!")
    elif x == paper:
        if pc == rock:
            player_win_counter += 1
            print("You win!")
        elif pc == scissors:
            pc_win_counter += 1
            print("Pc wins!")
        else:
            print("Draw!")
    elif x == rock:
        if pc == scissors:
            player_win_counter += 1
            print("You win!")
        elif pc == paper:
            pc_win_counter += 1
            print("Pc wins!")
        else:
            print("Draw!")
    else:
        print("Invalid input!")

    inp = input("Want to play again? (Y for yes / N for no): ").lower()
    if inp == "y":
        new_ans = input("Enter next move: ")
        rock_paper_scissors(new_ans)
    else:
        print(f"You won {player_win_counter} times, and Pc won {pc_win_counter} times.")

user_input = input("Enter Scissors, Paper, or Rock: ").lower()
rock_paper_scissors(user_input)