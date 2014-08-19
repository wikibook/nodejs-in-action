def find_two_smallest(L):
    '''Return a tuple of the indices of the two smallest values in list L.'''
    
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    
    put smallest back into L
    if min1 comes before min2, add 1 to min2
    return the two indices
