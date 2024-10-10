"""Here is a program with a function called "find_root" that uses bisectional search to search between low and low+step (where low is determined by find_root_range, with a low value of -10, and a high value of 10).  It is based on the bisectional search we did in our last class.


We can call it as follows: root_approximation = find_root(range_low, range_low+step, epsilon)
Does find_root work?  Why or why not?
"""
### ###########################################################################
### The function_with_roots whose roots we want to find: x^2-5
### ###########################################################################
def function_with_roots(value: float) -> float:
	result: float = (value ** 2) - 5
	return result

### ###########################################################################
### Exhaustive search to find the first root between low and high, at a
### resolution of step.
### ###########################################################################
def find_root_range(low, high, step):
	x1 = low
	x2 = low + step

	while (x2 < high):
			f_at_x1 = function_with_roots(x1)
			f_at_x2 = function_with_roots(x2)
			if (f_at_x1 * f_at_x2) <= 0:
				return x1
			    
			x1 = x2
			x2 += step
	return low-1

### ###########################################################################
### The find_root function, based on the bisectional search.  Does find_root
### work?  Why or why not?
### ###########################################################################
def find_root(low, high, epsilon):

		guess  = (high + low) / 2.0
		print(low)
		print(high)
		print(guess)
		result = function_with_roots(guess)
		
		while (abs(result) > epsilon):
			if (result > 0):
				low = guess
			elif (result < 0):
				high = guess
			else:
				return guess
			guess = (high + low) / 2.0
			result = function_with_roots(guess)
		return guess
		

### ###########################################################################
### The main program.  Search for roots between start and end, with a
### resolution of step for the exhaustive search and then search to within
### epsilon using bisectional search.
### ###########################################################################
start = -10.00
end = 10.00
step = 0.1
epsilon = 0.001

print(F"Searching for root between {start:.10f} and {end:.10f} ...")

range_low: float  = find_root_range(start, end, step)
range_high: float = range_low + step
print(range_low)
print(range_high)
if (range_low >= start and range_high <= end):

	root_approximation = find_root(range_low, range_high, epsilon)

	print(F"Root found between {range_low:.10f} and {range_high:.10f}.")
	print(F"Root approximation: x={root_approximation:.10f}, \
  f(x)={function_with_roots(root_approximation):.10f}")
else:
	print("Root not found within range")
