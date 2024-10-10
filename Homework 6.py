"""def largest_odd(w, x, y, z):
    largest = None
    for num in [w, x, y, z]:
        if num % 2 != 0:
            if largest is None or num > largest:
                largest = num
    
    if largest is None:
        return -1
    else:
        return largest
    """
"""def largest_odd(w=1, x=2, y=3, z=4):
    largest = None
    
    for num in [w, x, y, z]:
        if num % 2 != 0:
            if largest is None or num > largest:
                largest = num
    
    if largest is None:
        return -1
    else:
        return largest


print(largest_odd()) 
"""

"""def product(*values):
    product=1
    for a in values:
        product = product*a

    return product
print(product(2,3,4,5))
"""