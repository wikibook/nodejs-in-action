>>> birds = {'eagle' : 999, 'snow goose' : 33}
>>> if 'eagle' in birds:
...   print 'eagles have been seen'
...
eagles have been seen
>>> del birds['eagle']
>>> if 'eagle' in birds:
...   print 'oops: why are eagles still there?'
...
