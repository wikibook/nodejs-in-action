>>> values = [-1, 0, 1]
>>> for i in range(4):   # one more than len(values)
...     try:
...         r = 1.0 / values[i]
...         print 'reciprocal of', values[i], 'at', i, 'is', r
...     except IndexError:
...         print 'index', i, 'out of range'
...     except ArithmeticError:
...         print 'unable to calculate reciprocal of', values[i]
reciprocal of -1 at 0 is -1.0
unable to calculate reciprocal of 0
reciprocal of 1 at 2 is 1.0
index 3 out of range
