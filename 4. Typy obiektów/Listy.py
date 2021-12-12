L = [123, 'mielonka', 1.23]  # LISTY SĄ MODOWALNE!!!
L.append('NI')  # ".append" dodaję do listy na końcu
print(L)
L.pop(2)  # usuwanie z listy konkretnej jej skłdowej
print(L)
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M)  # macież 3x3 w postaci list zagnieżdżonych
print(M[1])  # podanie drugiego wiersza
print(M[1][2])  # podanie z drugiego wiersza, trzeciego elementu
col2 = [row[1] for row in M]  # zebranie elementów z drugiej kolumny, samam macierz pozostaje bez zmian
print(col2)
print(M)
diag = [M[i][i] for i in [0, 1, 2]]  # Pobieranie przekątnej z macierzy
print(diag)
print(list(range(4)))  # tworzenie listy od 0 do 3
print(list(range(-6, 7, 2)))  # tworzenie listy z przedziałem od -6 do + 6 z krokiem co dwa
print([[x ** 2, x ** 3] for x in range(4)])  # Wiele wartości, filtrowanie z użyciem polecenia if
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
