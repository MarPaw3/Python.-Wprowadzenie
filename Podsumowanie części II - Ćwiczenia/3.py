x = 'mielonka'; y = 'jajka'
x, y=y, x  #  zaminana wartości pod pozycjami
print(x, y)
d = {}
d[1] = 'a'; d[2] = 'b'
print(d)
d[(1, 2, 3)] = 'c'  # dodanie klucza 1, 2, 3 do wartości c
print(d[1, 2, 3])
d = {'a', 'b', 'c'}
d['d'] = 'mielonka'