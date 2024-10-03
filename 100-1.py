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
