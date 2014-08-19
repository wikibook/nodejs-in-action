scientists = {'Newton' : 1642, 'Darwin' : 1809, 'Turing' : 1912}

print 'keys:', scientists.keys()
print 'values:', scientists.values()
print 'items:', scientists.items()
print 'get:', scientists.get('Curie', 1867)

temp = {'Curie' : 1867, 'Hopper' : 1906, 'Franklin' : 1920}
scientists.update(temp)
print 'after update:', scientists

scientists.clear()
print 'after clear:', scientists
