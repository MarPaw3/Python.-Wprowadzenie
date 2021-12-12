D = {'a': 1, 'b':2, 'c':3}
print(D)
print('f' in D)  # odpowiedź dla f w zbiorze D = False
if not 'f' in D:  # jeżeli odpowiedź jest false w nowym akapicie print ...
    print('nie istnieje')
print(D)
for c in 'mielonka':  # pętla for
    print(c.upper())
x = 4
while x > 0:
    print('mielonka!' * x)
    x -= 1