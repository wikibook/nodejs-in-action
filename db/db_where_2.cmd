>>> cur.execute('SELECT Region FROM PopByRegion 
                 WHERE Population > 1000000 AND Region < "L"')
>>> print cur.fetchall()
[('Eastern Asia',))]
