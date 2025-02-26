# ####
# #Function that asks a user for a number and then we print in reverse

# number = int(input("Please enter the number that you want to print in reverse"))

# def reverse(n):
#     #base case
#     if n==0:
#         print(n)
#     else:
#         print (n)
#         reverse(n-1)
#         print (n)
# reverse(number)

# # Write a lamda function top check if a number is odd:

# check = lambda x:True if x%2 != 0 else False

# print(check(11))

# # write a lambda function to return the largest number between two inputs

# largest = lambda x,y: x if x>y else y

# print(largest(17,13))

# reverse = lambda x:x[::-1]
# print (reverse("hello"))

# numbers=(112,13,14,12)

# cube = map(lambda x: x**3, numbers)

# print(list(cube))
number = int(input("Enter a range number: "))

even = []  # List to store even numbers
odd = []   # List to store odd numbers

# Use lambda to check even or odd within a loop
for i in range (1,number):
    check_even = lambda x: x % 2 == 0  # Lambda for even check
    check_odd = lambda x: x % 3 == 0   # Lambda for odd check

    if check_even(i):  # Apply lambda for even
        even.append(i)
    elif check_odd(i):  # Apply lambda for odd
        odd.append(i)

print(f"{tuple(even)},{tuple(odd)}")