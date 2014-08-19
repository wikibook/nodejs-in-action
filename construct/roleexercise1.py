def find_last(filename, string):
    v0 = 0
    v1 = [None, None]
    v2 = open(filename, "r")
    for v3 in v2:
        v0 += 1
        if string in v3:
            v1 = [v0, v3]
    return v1
            
