x = 1
a = x  # współdzielą ten sam obiekt
a = 2  # Przestawia tylko 'a', 'x' jest nadal równy 1
print(x)
L = [1, 2]
b = L
b[0] = 'mielonka'
print(L)