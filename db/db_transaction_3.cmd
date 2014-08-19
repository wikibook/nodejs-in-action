Computer A: cur.execute('SELECT SignedOut FROM Books WHERE ISBN = "%s"' % isbn)
Computer A: signedOut = cur.fetchone()[0]
Computer B: cur.execute('SELECT SignedOut FROM Books WHERE ISBN = "%s"' % isbn)
Computer B: signedOut = cur.fetchone()[0]
Computer A: cur.execute('UPDATE Books SET SignedOut = %d 
                         WHERE ISBN = "%s"' % (signedOut + 1, isbn))
Computer A: cur.commit()
Computer B: cur.execute('UPDATE Books SET SignedOut = %d 
                         WHERE ISBN = "%s"' % (signedOut - 1, isbn))
Computer B: cur.commit()
