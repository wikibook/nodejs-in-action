>>> def describe_creature(name, species, age, weight):
...   return '%s (%s): %d years, %d kg' % (name, species, age, weight)
...
>>> print describe_creature(name='Charles Darwin', species='Homo sapiens', 
                            age=28, weight=70)
Charles Darwin (Homo sapiens): 28 years, 70 kg
