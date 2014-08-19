def find_min_max(values):
    '''Print the minimum and maximum value from the given collection of
    values.'''

    min = None
    max = None
    
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value
    
    print 'The minimum value is %s' % min
    print 'The maximum value is %s' % max
