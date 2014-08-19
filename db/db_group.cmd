>>> cur.execute('SELECT SUM (Population) FROM PopByCountry GROUP BY Region')
>>> cur.fetchall()
[(1364389,), (661200,)]
