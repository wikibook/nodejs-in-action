>>> def our_max(*values):
...     '''Find the maximum of any number of values.'''
...
...     if not values:
...         return None
...     m = values[0]
...     for v in values[1:]:
...         if v > m:
...             m = v
...     return m
...
>>> our_max(1)
1
>>> our_max(1, 2)
2
>>> our_max(3, 1, 2, 5, 4, -17)
5
