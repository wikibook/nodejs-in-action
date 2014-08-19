def read_all_molecules(r):
    '''Read zero or more molecules from reader r,
    returning a list of the molecules read.'''

    result = []
    line = r.readline()
    while line:
        molecule, line = read_molecule(r, line)
        result.append(molecule)
    return result
