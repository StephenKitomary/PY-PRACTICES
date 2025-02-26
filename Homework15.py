
def is_prime_recursive(integer, divisor=None):
    if divisor is None:
        divisor = integer - 1
    if divisor == 1:
        return True
    if integer % divisor == 0:
        return False
    # Recursion block
    return is_prime_recursive(integer, divisor - 1)

integer = int(input("Enter a positive integer greater than 1 to check if it is prime: "))

if integer <= 1:
    print("Input must be greater than 1.")
    exit()

prime = is_prime_recursive(integer)

if prime:
    print(f"{integer} is prime.")
else:
    print(f"{integer} is not prime.")


###############################################################################################

def bisection_search_recursive(low, high, epsilon, iterations=0):
    guess = (high + low) / 2.0
    result = guess ** 2 - 3

    print(f"Iteration: {iterations}, Guess: {guess}, Result: {result}")

    if abs(result) <= epsilon:
        return guess

    if result > 0:  
        return bisection_search_recursive(low, guess, epsilon, iterations + 1)
    else:  
        return bisection_search_recursive(guess, high, epsilon, iterations + 1)
low = 0.0  
high = 3.0  
epsilon = 0.001  


result = bisection_search_recursive(low, high, epsilon)


print(f"Final approximation: {result}")
