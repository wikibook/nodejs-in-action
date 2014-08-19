import sys

# Find all the birds.
birds = []
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    # For each bird, find its entry and increment the count.
    for line in infile:
        name = line.strip()
        found = False
        for entry in birds:
            if entry[0] == name:
                entry[1] += 1
                found = True
        if not found:
            birds.append([name, 1])
    infile.close()
# Print.
for (name, count) in birds:
    print name, count
