import math

# =============================================================================
# Figuring out (x,y) given position n in the enumeration may be done as
# follows.  This strategy inverts the Cantor pairing (which takes the pair
# as input, and returns the element).
# =============================================================================
def pair(n):
    w = int((math.sqrt(8*n + 1) - 1) // 2)
    t = n - (w*(w+1)) // 2
    return (w - t, t)

# =============================================================================
# Doing the same with triples is more complicated, because it requires cubics.
# An easier way is to use a walk.  To make this simple, I'll first present
# the walk for pairs.  Then we'll do a walk for triples.
# =============================================================================
def pair_walk(n):

    # Let the "height" of a pair be the sum of the elements of that pair.
    # So, when h=0, there is one pair: (0,0)
    # And when h=1, there are two pair: (1,0), (0,1)
    # And when h=2, there are three pair: (2,0), (1,1), (0,2).
    # In general a height h has exactly h+1 pairs.

    # The total number of pairs with sums less than or equal to h is given by
    # a formula for a triangular number, where T(h+1) = [(h+1)*(h+2)]//2.
    #
    # Here, we are looking for the smallest h such that T(h+1) > n.  Once we
    # have it, we know the number of pairs that have come before height h.
    h = 0
    while n >= (h + 1) * (h + 2) // 2:
        h += 1
  
    # The offset within the height gives us the position in the list of pairs
    # for the height.  By calculating the offset, we can then create the pair.
    offset = n - (h * (h + 1) // 2)
    return (h - offset, offset)

# =============================================================================
# We can then do the same for triples.  It's a little more complex, but the
# strategy is the same.
# =============================================================================
def triple_walk(n):

    # Find the height and offset
    h = 0
    cumulative = 0
    found_it = False
    while not found_it:
        count = (h + 1) * (h + 2) // 2
        if cumulative + count > n:
            found_it = True
        else:
            cumulative += count
            h += 1
    offset = n - cumulative
 
    # Generate all triples for height h
    triples = [(x, y, h - x - y)
        for x in range(h + 1)
        for y in range(h - x + 1)]

    return triples[offset]

# =============================================================================
# Print out lists of the first p tuples.
# =============================================================================
p = 3
print(pair(p))
# print([pair_walk(x) for x in range(p)])
# print([triple_walk(x) for x in range(p)])
