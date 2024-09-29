from random import randint
print("######################################")
print("#    ROCK PAPER SCISSOR GAME         #")
print("######################################")
computer_choice = randint(1,3)
user_choice=int(input("Please enter your input:\n1. Rock\n2. Scissor\n3. Paper\n"))
if user_choice == 1 or user_choice == 2 or user_choice == 3: 
    if user_choice == computer_choice:
        print("It's a tie!")
        print(f"The computer choice was {computer_choice}")
    elif user_choice - computer_choice == 2:
        print("You win!")
        print(f"The computer choice was {computer_choice}")
    elif user_choice - computer_choice == -1:
        print("You win!")
        print(f"The computer choice was {computer_choice}")
    else:
        print("The computer Wins")
        print(f"The computer choice was {computer_choice}")
else:
    print("Wrong Input, follow the instructions")

