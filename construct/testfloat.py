from math import abs
from mylibrary import average

test_cases = [
    [0.0, [ 0.0]],
    [0.0, [-1.0,  1.0]],
    [1.0, [ 0.0,  2.0]],
    [2.0, [ 0.0,  1.0, 2.0, 3.0, 4.0]],
    ....
]

passes = failures = 0
for (expected, values) in test_cases:
    actual = average(values)
    if actual == expected:
        passes += 1
    else:
        failures += 1

print 'passes:', passes
print 'failures:', failures
