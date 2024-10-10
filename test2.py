def find_root_range(x,z):
    while True:
        checknumber= (x**4)+(x**3)+(5*(x**2))-50
        if checknumber > 0:
            x=x+z
        
        else:
            return x
x = find_root_range(-10,0.000001)
print(f"the upper bound is {x}")
print(f"the lower bound is {x-0.000001}")