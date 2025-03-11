"""
##Required to do the following:

1. See what the code does
2.Write a specification for it
3.Write a series of black box tests for it
4.Add exceptions to the code
5.Write a series of glassbox test to it
"""
def non_primes(low,high):
    """
        Returns a list of all the non_prime number between the low and the high(inclusive)

        Pre-requisites:
        * Positional argument 0(low) should indeed be less than the Positional argument1(high)
        * The range should be between non-negative numbers
    """
    results = []

    for number in range (low, high+1):
        is_non_prime = False

        for divisor in range(2, int(number**(1/2)+1)):
            if number % divisor == 0:
                is_non_prime = True
                break
        if is_non_prime:
            results.append(number)

    return results
print(non_primes(10,0))
