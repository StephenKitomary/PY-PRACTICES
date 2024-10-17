def log(x, base, epsilon):
    """Assumes x  and  epsilon int or float, base an int,
        x > 1, epsilon > 0 & power >= 1
        Returns folat y such that base**y is within epsilon of x."""
    lower_bound = 0
    while 2**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    #Perform the bisection search
    ans  = (high +low)/2
    while abs(base**ans-x) >= epsilon:
        if (base**ans < x):
            low =ans