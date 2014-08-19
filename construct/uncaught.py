values = [-1, 0, 1]
for i in range(4):   # one more than len(values)
    try:
        r = 1.0 / values[i]
        print 'reciprocal of', values[i], 'at', i, 'is', r
    except IndexError, e:
        print 'error:', e
