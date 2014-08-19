import sys
from tsdl import skip_header
def smallest_value_skip(r):
    '''Read and process reader r to find the smallest value after 
    the TSDL header.  Skip missing values, which are indicated 
    with a hyphen.'''
    line = skip_header(r).strip()

    # Now line contains the first data value; this is also the
    # smallest value found so far.
    smallest = int(line)
    for line in r:
        line = line.strip()

        # Only process line if it has a valid value.
        if line != '-':
            value = int(line)

            # Process value; if we find a smaller value, remember it.
            if value < smallest:
                smallest = value

    return smallest
if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    print smallest_value_skip(input_file)
    input_file.close()
