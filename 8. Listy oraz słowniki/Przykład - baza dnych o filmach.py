table = {'1975' : 'Monty Python i Święty Graal', '1979' : 'Żywot Briana', '1983' : 'Sens życia według Monty Pythona'}
print(table)
year = '1983'
movie = table[year]  # słownik[klucz] => wartość
print(movie)
for year in table:  # To samo co : for year i table.keys()
    print(year + '\t' + table[year])
K = 'Monty Python i Święty Graal'
