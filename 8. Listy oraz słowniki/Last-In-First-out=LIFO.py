L = []
L.append(1)  # Wstawiene na stos
L.append(2)
L.extend('mielonka')
L.reverse()
L.count('mielonka')
print(L)
L.pop()  # usunięcie ostatniego elementu ze stosu
print(L.count(1))
print(L.index(2))
print(L)