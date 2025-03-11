"""
##Required to do the following:

1. See what the code does
2.Write a specification for it
3.Write a series of black box tests for it
4.Add exceptions to the code
5.Write a series of glassbox test to it
"""

#%%writefile Non_Primes.py

def non_primes(low,high):
    """
        Returns a list of all the non_prime number between the low and the high(inclusive)

        Pre-requisites:
        * Positional argument 0(low) should indeed be less than the Positional argument1(high)
        * The range should be between non-negative numbers
    """

    try:
        if not (type(low) is int or type(high) is int):
            print(type(low),type(high))
            raise TypeError("Both the Low and High should be integers")

        if low < 0 or high < 0:
            raise ValueError("Low and High must be non-negative numbers")

        if low >= high:
            raise ValueError("Invalid Range, low must be less than high")
            
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

    except TypeError:
        print("Both the high and the Low should be Intergers")
    except ValueError:
        print("Low and high but be non negative integers and low must be less than the high")
        

def test_valid_range():
    
    assert non_primes(10,20) == [10, 12, 14, 15, 16, 18, 20]

def test_invalid_range():
    assert non_primes(10,5)==[]

def test_invalid_type():
    pass

    
print(non_primes(2.66,100))
