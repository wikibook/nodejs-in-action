def non_blank_lines(thing):
    '''Return the number of non-blank lines in thing.'''
    
    count = 0
    for line in thing:
        if line.strip():
            count += 1
    return count
