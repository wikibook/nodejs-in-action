>>> cur.execute('SELECT SUM (Population) FROM PopByRegion')
>>> cur.fetchone()
(8965762,)
