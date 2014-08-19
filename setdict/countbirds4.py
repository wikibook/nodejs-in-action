import sys

# Count all the birds.
count = {}
for filename in sys.argv[1:]:
    infile = open(filename, 'r')
    for line in infile:
        name = line.strip()
        count[name] = count.get(name, 0) + 1
    infile.close()

# Invert the dictionary.
freq = {}
for (name, times) in count.items():
    if times in freq:
        freq[times].append(name)
    else:
        freq[times] = [name]

# Print.
for key in sorted(freq):
    print key
    for name in freq[key]:
        print ' ', name
