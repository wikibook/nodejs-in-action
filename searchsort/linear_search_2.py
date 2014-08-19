def linear_search(v, L):
    '''Return the index of the first occurrence of v in list L, or return len(L)
    if v is not in L.'''
    
    i = 0
    for value in L:
        if value == v:
            return i
        i += 1
    return len(L)