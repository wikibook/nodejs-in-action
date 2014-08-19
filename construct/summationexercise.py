def summation(limit):
    '''Return the sum of the numbers from 0 to limit.'''

    total = 0
    current = limit
    while current != 0:
        total += current
        current -= 1
    return total