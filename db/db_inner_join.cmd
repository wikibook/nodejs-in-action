>>> cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country 
FROM   PopByRegion INNER JOIN PopByCountry 
WHERE  (PopByRegion.Region = PopByCountry.Region) 
AND    (PopByRegion.Population > 1000000)
''')
>>> print cur.fetchall()
[('Eastern Asia', 'China'), ('Eastern Asia', 'DPR Korea'), 
('Eastern Asia', 'Hong Kong (China)'), ('Eastern Asia', 'Mongolia'), 
('Eastern Asia', 'Republic of Korea'), ('Eastern Asia', 'Taiwan')]
