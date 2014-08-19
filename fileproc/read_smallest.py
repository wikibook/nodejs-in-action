import sys
import tsdl

def smallest_value(r):
    '''Read and process reader r to find the smallest
    value after the TSDL header.'''
    line = tsdl.skip_header(r).strip()
	
    # Now line contains the first data value; this is also the
    # smallest value found so far, because it is the only one we have seen.
    smallest = int(line)
    for line in r:
        line = line.strip()
        value = int(line)

        # If we find a smaller value, remember it.
        if value < smallest:
            smallest = value
    return smallest
	
if __name__ == "__main__":
    input_file = open(sys.argv[1], "r")
    print smallest_value(input_file)
    input_file.close()