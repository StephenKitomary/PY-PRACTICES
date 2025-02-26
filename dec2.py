def fibonacci_recursive(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
fibonacci_recursive(5)

##################################################################################

def fibonacci_recursive(n, sum =1):
    if n == 0:
        return sum
    elif n == 1:
        return sum
    else:
        sum =
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
fibonacci_recursive(5)