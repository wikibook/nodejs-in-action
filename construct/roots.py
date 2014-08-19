from math import sqrt

def roots(a, b, c):
    '''Return real roots of a quadratic, or None.'''
    temp = b**2 - 4*a*c
    if temp < 0:
        return None
    temp = sqrt(temp)
    left = (-b + temp) / (2 * a)
    right = (-b - temp) / (2 * a)
    return left, right
