>>> values = [-1, 0, 1]
>>> for i in range(4):   # one more than len(values)
...     try:
...         r = 1.0 / values[i]
...         print 'reciprocal of', values[i], 'at', i, 'is', r
...     except IndexError, e:
...         print 'error:', e
...     except ArithmeticError, e:
...         print 'error:', e
reciprocal of -1 at 0 is -1.0
error: float division
reciprocal of 1 at 2 is 1.0
error: list index out of range
