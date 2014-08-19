Bases = set(["Mg"]) # nothing but magnesium
Acids = set(["Cl"]) # nothing but chlorine

def test_MgCl():
    '''Works if the base is a base, and the acid is an acid.'''

    assert is_salt("Mg", "Cl")

def test_ArCl():
    '''Doesn't work because the 'base' isn't a base.'''

    assert not is_salt("Ar", "Cl")

def test_MgO():
    '''Doesn't work because the 'acid' isn't an acid.'''

    assert not is_salt("Mg", "O")

def test_neither():
    '''Doesn't work because neither is right.'''

    assert not is_salt("Ar", "O")

