"""
print("Hello "+input("What is your name?"))

name = str(input("what is your name?"))

print(f"hello {name}! How are you doing today?")

"""
"""
print("Welcome to the Brand Name Generator")
city = str(input("Whats the name of the city that you grew up in?\n"))
pet = str(input("What's your pet's name?\n"))
print(f"Your brand name could be {city} {pet}")
"""
"""
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = total + ((tip/100)*total)
each = round(total_tip/people, 2)

print(f"Each person should pay: ${each}")
"""
"""
names = input("Gemme the names of the people separated by a comma")

names_list = names.split(",")

print(names_list[0])
"""
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = int(input("Where do you want to put the treasure?"))

position_string =str(position)
column = position_string[0]
column_int = int(column)
row = position_string[1]
row_int = int(row)
if row_int== 1:
    row1[column_int-1] = "X"

elif row_int== 2:
    row2[column_int-1] = "X"

elif row_int== 3:
    row3[column_int-1] = "X"

else:
    print("Invalid number")

print(f"{row1}\n{row2}\n{row3}")