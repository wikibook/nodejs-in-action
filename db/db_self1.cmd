>>> cur.execute('SELECT Country FROM PopByCountry 
                 WHERE (ABS(Population - Population) < 1000)')
>>> cur.fetchall()
[('China',), ('DPR Korea',), ('Hong Kong (China)',), ('Mongolia',), 
('Republic of Korea',), ('Taiwan',), ('Bahamas',), ('Canada',), 
('Greenland',), ('Mexico',), ('United States',)]

