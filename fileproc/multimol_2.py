def read_molecule(r):
    '''Read a single molecule from reader r and return it,
    or return None to signal end of file.'''

    # If there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND   name"
    key, name = line.split()
    
    # Other lines are either "END" or "ATOM num type x y z"
    molecule = [name]
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, type, x, y, z = line.split()
            molecule.append((type, x, y, z))

    return molecule
