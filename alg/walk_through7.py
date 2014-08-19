def find_two_smallest(L):
    '''Return a tuple of the indices of the two smallest values in list L.'''
    # set min1 and min2 to the indices of the smallest and next-smallest
    # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min2, min1 = 1, 0
    # examine each value in the list in order
    for i in range(2, len(L)):
        # L[i] is larger than both min1 and min2, smaller than both, or
        # in between.
        # New smallest?
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        # New second smallest?
        elif L[i] < L[min2]:
            min2 = i
    return (min1, min2)
