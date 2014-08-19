>>> def divide(top, bottom):
...     if bottom == 0:
...         raise ValueError('divisor is zero')
...     else:
...         return top / bottom
... 
>>> for i in range(-1, 2):
...     try:
...         print divide(1, i)
...     except ValueError, e:
...         print 'caught exception for', i
...
-1
caught exception for 0
1
