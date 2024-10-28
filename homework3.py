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