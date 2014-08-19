>>> cur.execute('INSERT INTO Test VALUES (NULL, 456789)')
Traceback (most recent call last):
  File "<string>", line 1, in <string>
sqlite3.dbapi2.IntegrityError: Test.Region may not be NULL

