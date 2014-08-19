def print_table():
    '''Print the multiplication table for numbers 1 through 5.'''
    numbers = [1, 2, 3, 4, 5]
    # Print the header row.
    for i in numbers:
        print '\t' + str(i),
    print # End the header row.
    # Print the column number and the contents of the table.
    for i in numbers:
        print i,
        for j in numbers:
            print '\t' + str(i * j),
        print # End the current row.
