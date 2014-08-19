import sys
from tsdl import skip_header

def process_file(r):
    '''Read and process reader r.'''

    line = skip_header(r).strip()

    # The largest value seen so far.
    largest = -1

    for value in line.split():

        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    # Check the rest of the lines for larger values.
    for line in r:
        # The largest value seen so far.
        large = -1

        for value in line.split():

            # Remove the trailing period.
            v = int(value[:-1])
            # If we find a larger value, remember it.
            if v > large:
                large = v

        if large > largest:
            largest = large

    return largest
if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    print process_file(input_file)
    input_file.close()
