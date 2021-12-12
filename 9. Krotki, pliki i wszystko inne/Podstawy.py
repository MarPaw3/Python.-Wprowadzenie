print((1 + 2) + (3 + 4))
T = (1, 2, 3, 4)
L = [x + 20 for x in T]
print(L)
T = (1,2,3,4,6,8,3,1,2)
print(T.index(2))  # Offset pierwszego wystąpieni elementu o wartości 2
print(T.count(2))  # Ile jest elementów o wartości 2?
T = (1, [2, 3], 4)
print(T)
#  T[1] = 'mielonka'  # nie można zmienić krotki
T[1][0] = 'mielonka'  # można zmienić listę w krotce
print(T)