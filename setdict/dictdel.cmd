>>> birds = {'snow goose' : 33, 'eagle' : 9}
>>> del birds['snow goose']
>>> birds
{'eagle' : 9}
>>> del birds['gannet']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'gannet'
