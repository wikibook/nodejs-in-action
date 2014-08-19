>>> cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
>>> print cur.fetchall()
[('Northern Africa',), ('Southern Asia',), ('Eastern Asia',))]
