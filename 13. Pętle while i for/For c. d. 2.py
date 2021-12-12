d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key, '=>', d[key])  # użycie iteratora po kluczach słownika i indeksowania

list(d.items())
for (key, value) in d.items():
    print(key, '=>', value)  # iteracja po kluczach i wartościach