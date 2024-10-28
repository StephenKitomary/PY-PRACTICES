"""word = input("Please enter your word")

for i in word:
    print(i)
for i in word[::-1]:
    print(i)

"""
"""
word = input("please enter a word:")
letter = input("please enter a letter ro remove")
hangman=[]

for i in word:
    if i == letter:
        hangman.append("_")
    else:
        hangman.append(i)

print(hangman)
"""
"""
# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Ask the user for how many Fibonacci numbers they want to generate
num = int(input("How many Fibonacci numbers would you like to generate? "))

# Generate and print the Fibonacci sequence
if num <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci(num)
    print("The first", num, "Fibonacci numbers are:")
    for number in fibonacci_sequence:
        print(number)
"""