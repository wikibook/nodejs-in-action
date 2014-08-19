def largest_below_threshold(values, threshold):
    '''Find the largest value below a specified threshold. If no value is 
    found, returns None.'''
    
    result = None
    for v in values:
        if v < threshold:
            result = v
            break
            
    if result is None:
        return None
    
    for v in values:
        if result < v < threshold:
            result = v
    return result