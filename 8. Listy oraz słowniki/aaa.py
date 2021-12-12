res = []  # utworzenie pustej listy
for c in 'jajko':  # dla liter w 'jajko': odpowiednik listy składanej
    res.append(c*4)
print(res)
L  = ['mielonka', 'Mielonka', 'MIELONKA!']
print(L[-2:])
matrix = [[1, 2, 3], [4, 5, 5],[7, 8, 9]]  # Tworzenie listy zagnieżdżonych w listach daję macież
print(matrix[1][1])  #  wywołanie z listy 1 (2-ej) wartości 1 (2-ej), liczone od zera
L = [1, 2, 3]
L[1:2] = [4, 5]  # zmiana/wstawienie
print(L)
L[1:1] = [6, 7]
print(L)  # wstawienie ( nic nie usuwamy)
L[1:2] = []  # usuwanie
print(L)