def total(values, start=0, end=None):
    '''Add up the values in a list. If none are given, the total is zero. If
    'start' is not specified, start at the beginning. If 'end' is specified,
    go up to but not including that index; otherwise, go to the end of the
    list.'''

    if not values:
        return 0

    if end is None:
        end = len(values)

    result = 0
    for i in range(start, end):
        result += values[i]
    return result
