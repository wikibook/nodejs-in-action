def compute_reciprocals(values):
    '''Return a list of the reciprocals of the given list of values. 
    If a value has no reciprocal, it will be assigned a value of 
    None in the returned list.'''

    reciprocals = []
    for value in values:
        reciprocals.append(1 / value)
    return reciprocals
