D = {}
D[999] = 'mielonka'  # Dodanie do słownika D pod kluczem 999 wartości mielonka
print(D)
table = {1975 : 'Święty Graal', 1979 : 'Żywot Briana', 1983 : 'Sens życia'}
print(list(table.items()))
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2; Y = 3; Z = 4  # Średnik rozdziela polecenia
print(Matrix[(X, Y, Z)])
print(Matrix)
if (2, 3, 6) in Matrix:  # Sprawdzenie kluczy przed pobraniem
    print(Matrix[(2, 3, 6)])
else:
    print(0)
try:  # próba indeksowania
    print(Matrix[(2, 3, 6)])
except KeyError:  # Przechwycenie i obsługa błedu
    print(0)
print(Matrix.get((2, 3, 4), 0))  # Istnieje - pobieramy i zwracamy wartość
print(Matrix.get((2, 3, 6), 0))  # Nie istnieje - używamy warości domyślnej

