print('Welcome to Tressure Island.\nYour mission is to find the tressure.')

choice = input("left or right?")
if choice.lower() == "right":
    print("Game Over.")

else:
    choice = input("swim or wait?")
    if choice.lower() == "swim":
        print("Game Over.")
        
    else:
        choice = input("Which door?(Blue, yellow,red)")
        if choice.lower() == "blue":
            print("Game Over.")
        elif choice.lower() == "red":
            print("Game Over.")

        elif choice.lower() == "yellow":
            print("You Win!")
        else:
            
            print("Invalid Choice")

