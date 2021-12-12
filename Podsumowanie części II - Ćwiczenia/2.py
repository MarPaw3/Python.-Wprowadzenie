l = [1, 2, 3] + [4, 5, 6]
l.reverse(); print(l)
l.sort(); print(l)
print(l.index(4))  # drukuj z listy l pozycje 4wartą od zera
print(({'a': 1, 'y': 2},['b']))
d = {'x': 1, 'y': 2, 'z': 3}
d['w'] = 0
print(d['x'] + d['w'])
d[(1, 2, 3)] = 4  # dodanie do słownika krotki z szeregiem liczb jako klucz do wartości 4:)
print(d)
print(list(d.keys()))  # wartości kluczy dla słownika d
print(list(d.values()))  # wartości w słowniku
print((1, 2, 3) in d)  # Czy wartości 1, 2, 3 znajdują się w słowniku
print([[]], ['',[],(),{}, None])
print(l[12:24])
del l[0:]; print(l)