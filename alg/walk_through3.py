def find_two_smallest(L):
    '''Return a tuple of the indices of the two smallest values in list L.'''
    
    set min1 and min2 to the indices of the smallest and next-smallest
    values at the beginning of L
    
    examine each value in the list in order
        update these values when a new smaller value is found
    return the two indices
