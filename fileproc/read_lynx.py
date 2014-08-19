import sys
from tsdl import skip_header

def find_largest(line):
    '''Return the largest value in line, which is a
    whitespace-delimited string of integers.'''
    # The largest value seen so far.
    largest = -1

    for value in line.split():

        # Remove the trailing period.
        v = int(value[:-1])

        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

def process_file(r):
    '''Read and process reader r.'''
    line = skip_header(r).strip()

    # The largest value so far.
    largest = find_largest(line)

    # Check the rest of the lines for larger values.
    for line in r:
        large = find_largest(line)
        if large > largest:
            largest = large

    return largest
if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    print process_file(input_file)
    input_file.close()
