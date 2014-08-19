>>> cur.execute('''
SELECT DISTINCT Region 
FROM            PopByCountry 
WHERE           Region NOT IN 
    (SELECT DISTINCT Region 
     FROM            PopByCountry 
     WHERE           (PopByCountry.Population = 8764))
''')
>>> cur.fetchall()
[('North America',)]
