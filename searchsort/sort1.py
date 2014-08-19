def find_largest(N, L):
    """Return the N largest values in L in order from smallest to largest."""

    copy = L[:]
    copy.sort()
    return copy[:N]
