# Afunction that finds the hamonic sum 
# number = int(input("Enter the number you want to find harmonic sum for"))

# def harmonic_sum(n):
#     if n == 1:
#         return (1/n)
#     else:
#         return ((1/n)+ harmonic_sum(n-1))
    
# print(harmonic_sum(number))

# n = int(input("enter range:"))

# even = []
# odd = []

# for i in range(1,n):
#     check_even = lambda x: x%2 == 0
#     check_odd = lambda x: x%3 == 0

#     if check_even(i):
#         even.append(i)
#     elif check_odd(i):
#         odd.append(i)
    
# print(tuple(even), tuple(odd))

number = int(input("Please enter the number that you want to print in reverse: "))

def reverse(n):
    # Base case
    if n == 0:
        print(n)
    else:
        print(n)  # Print the current number
        reverse(n - 1)  # Recursive call
        print(-n)  # Print the number again after the recursive call

reverse(number)
