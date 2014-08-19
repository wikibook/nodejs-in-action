cur.execute('SELECT SignedOut FROM Books WHERE ISBN = "%s"' % isbn)
signedOut = cur.fetchone()[0]
cur.execute('UPDATE Books SET SignedOut = %d 
             WHERE ISBN = "%s"' % (signedOut + 1, isbn))
cur.commit()
