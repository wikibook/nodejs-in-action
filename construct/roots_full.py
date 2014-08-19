from math import sqrt
def roots(a, b, c):
    '''Return real roots of a quadratic, or None.'''
    if sqrt(b**2 - 4*a*c) < 0:
        return None
    left = (-b + sqrt(b*2 - 4*a*c)) / (2 * a)
    right = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    return left, right
