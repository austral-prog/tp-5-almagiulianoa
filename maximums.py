def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y :
        return x 
    else :
        return y

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y 
    if z > x and z > y:
        return z
    if x == z and z == y:
        return x  
