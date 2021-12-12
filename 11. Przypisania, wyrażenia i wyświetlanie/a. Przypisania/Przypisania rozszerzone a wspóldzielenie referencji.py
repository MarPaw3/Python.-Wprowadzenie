l = [1, 2]
m = l  # l i m są referencjami do jednego obiektu
l = l + [3, 4]  # konkatenacja tworzy nowy obiekt
print(l, m)  # zmiana l, ale nie m
l = [1, 2]
m = l
l += [3, 4]  # += ozacza użycie extend
print(l, m)  # Również w m zmiana jest widoczna
