def read_molecule(r, line):
    '''Read a molecule from reader r.  The variable 'line'
    is the first line of the molecule to be read; the result is
    the molecule, and the first line after it (or the empty string
    if the end of file has been reached).'''

    fields = line.split()
    molecule = [fields[1]]

    line = r.readline()    
    while line and not line.startswith('COMPND'):
        fields = line.split()
        key, num, type, x, y, z = fields
        molecule.append((type, x, y, z))
        line = r.readline()

    return molecule, line
