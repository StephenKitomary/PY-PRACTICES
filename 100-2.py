"""print('Welcome to Tressure Island.\nYour mission is to find the tressure.')

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
""" 

"""students = input("Input a list of student heights ").split()
print(students)
answer = 0 
for n in range(0, len(students)):
    students[n] = int(students[n])
    answer = answer + students[n]

print(students)
print(sum(students))
print(answer)
"""

for i in range (1,101):
    if i%3==0 and i%5 == 0:
        print("Fizzbuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
