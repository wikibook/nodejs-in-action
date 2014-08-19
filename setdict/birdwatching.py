import sys

# Find the different bird types observed.
birds = set()
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    for line in infile:
        name = line.strip()
        birds.add(name)
    infile.close()

# Print the birds.
for b in birds:
    print b
