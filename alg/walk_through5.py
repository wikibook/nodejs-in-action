def find_two_smallest(L):
    '''Return a tuple of the indices of the two smallest values in list L.'''
    
    # set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min2, min1 = 0, 1
    
    # examine each value in the list in order
    for i in range(2, len(values)):
        update min1 and/or min2 when a new smaller value is found
    return the two indices
