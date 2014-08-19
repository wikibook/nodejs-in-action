>>> cur.execute('''
SELECT DISTINCT Region 
FROM            PopByCountry 
WHERE           (PopByCountry.Population != 8764)
''')
>>> cur.fetchall()
[('Eastern Asia',), ('North America',)]
