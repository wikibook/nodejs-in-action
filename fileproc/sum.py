def sum(input_file, output_filename):
    '''Reads the data from open file descriptor input_file, which contains
    two floats per line separated by a space.  For each line from 
    input_file, a line is written to the file named output_filename
    containing the two floats from the corresponding line of input_file
    plus a space and the sum of the two floats.'''
	
    output_file = open(output_filename, 'w')
	
    for line in input_file:
        operands = line.split()
        print 'operands', operands
        sum = float(operands[0]) + float(operands[1])
        new_line = line.rstrip() + ' ' + str(sum) + '\n'
        output_file.write(new_line)
    output_file.close()
