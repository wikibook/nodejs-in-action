import bisect

def bin_sort(values):
    '''Sort values, creating a new list.'''
    result = []
    for v in values:
        bisect.insort_left(result, v)
    return result
