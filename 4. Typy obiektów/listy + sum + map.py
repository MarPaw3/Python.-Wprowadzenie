M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
G = (sum(row) for row in M)  # utworzenie generatora sum wierszy
print(next(G))  # użycie funkcji
print(next(G))
print(next(G))
print(list(map(sum, M)))  # Wykonanie funkcji "sum" dla elementów macierzy M
print({sum(row) for row in M})  # Utworzenie zbioru sum wierszy
print({i : sum(M[i]) for i in range(3)})  # Utworzenie tabeli klucz-wartość sum wierszy
print([ord(x) for x in 'mieloonka'])  # Lista numerów porządkowych znaków LISTA = [LISTA]
print({ord(x) for x in 'mieloonka'})  # Zbiór pozwala na usunięcie duplikatów ZIÓR = {ZBIÓR}

