from math import sqrt

def standard_deviation(values):
    v0 = 0.0
    for v1 in values:
        v0 += v1
    v2 = v0 / len(values)
    v3 = 0.0
    for v4 in values:
        v3 += (v4 - v2) ** 2
    v5 = v3 / len(values)
    return sqrt(v5)