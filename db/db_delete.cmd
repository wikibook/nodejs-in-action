>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
>>> cur.execute('SELECT * FROM PopByRegion');
>>> cur.fetchall()
[('Southeastern Africa', 743112), ('Northern Africa', 1037463),
('Southern Asia', 2051941), ('Middle East', 687630), ('South America',
593121), ('North America', 661157), ('Western Europe', 387933)]
