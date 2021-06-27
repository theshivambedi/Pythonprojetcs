import random
user_choice = input("choose between rock, paper and scissor\n")
a = user_choice.lower()
game = ("rock","paper","scissor")
computer_choice = game[random.randint(0, len(game)-1)]

if a == "rock" and computer_choice == "paper":
    print("computer choice is Paper, you lose")
elif a == "rock" and computer_choice == "scissor":
    print("Computer choice is scissor, you win")
elif a == "rock" and computer_choice == "rock":
    print("computer choice is rock, game is draw")    
elif a == "paper" and computer_choice == "paper":
    print("computer choice is Paper, game is draw")
elif a == "paper" and computer_choice == "scissor":
    print("Computer choice is scissor, you lose")
elif a == "paper" and computer_choice == "rock":
    print("computer choice is rock, you win")  
elif a == "scissor" and computer_choice == "paper":
    print("computer choice is Paper, you win")
elif a == "scissor" and computer_choice == "scissor":
    print("Computer choice is scissor, game is drawn")
elif a == "scissor" and computer_choice == "rock":
    print("computer choice is rock, you lose")
else:
    print("The input you are putting is invalid. Please put the correct input")        