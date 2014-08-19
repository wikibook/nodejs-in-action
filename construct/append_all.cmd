>>> def append_all(old, *new):
...     for n in new:
...         old.append(n)
...     return old
...
>>> values = []
>>> append_all(values, 1, 2, 3)
[1, 2, 3]
>>> append_all(values) # not actually appending anything
[1, 2, 3]
