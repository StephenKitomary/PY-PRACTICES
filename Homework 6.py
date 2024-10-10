def largest_odd(w, x, y, z):
    largest = None
    for num in [w, x, y, z]:
        if num % 2 != 0:
            if largest is None or num > largest:
                largest = num
    
    if largest is None:
        return -1
    else:
        return largest