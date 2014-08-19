>>> def invert(x):
...     try:
...         i = 1.0 / x
...     except:
...         print 'caught exception for', x
...     else:
...         print 'reciprocal of', x, 'is', i
... 
>>> invert(1)  
reciprocal of 1 is 1.0
>>> invert(0)
caught exception for 0
