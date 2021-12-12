d = {'mielonka': 2, 'jajka': 3, 'szynka': 1}
print(d.keys())  # pokazuje klucze zawarte w słowniku
print('pomidory' in d)  # sprawdza czy słownik zawiera wartość pytaną
print(list(d.keys()))
print(d)
d['szynka'] = ['grillowanie', 'pieczenie', 'smażenie']  # Zmiana wpisu (wartość = lista)
print(d)
del d['jajka']  # usunięcie wpisu
print(d)
d['lunch'] = 'Bekon'  # Dodanie nowego wpisu
print(d)
d = {'mielonka': 2, 'jajka': 3, 'szynka': 1}
print(list(d.values()))
print(list(d.items()))
print(d.get('mielonka'))  # Klucz istnieje
print(d.get('tost'))  # Niesistniejący klucz