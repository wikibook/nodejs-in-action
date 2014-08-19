def after_date(input_file, date):
    '''Return the lines that were added to a file after a certain date.'''
    keep_it = False
    result = []
    for line in input_file:
        if keep_it:
            result.append(line)
        elif get_date(line) >= date:
            keep_it = True
    return result
