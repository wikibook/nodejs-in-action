def linear_search(v, L):
    '''Return the index of the first occurrence of v in list L, or return len(L)
    if v is not in L.'''
    i = 0
    # Keep going until we reach the end of L or until we find v.
    while i != len(L) and L[i] != v:
        i = i + 1
    return i
