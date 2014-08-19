def process_file(filename):
    '''Read and print the contents of a file.'''
    
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        print line
