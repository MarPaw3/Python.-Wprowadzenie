s = {1.23}
#s.add([1, 2, 3])  # W ziorze mogą znajdować się jedynie obiekty niemutowalne no lisy
#s.add({'a' : 1})  # ani słowniki no dict
s.add((1, 2, 3))  # krotki są OK
print(s | {(4, 5, 6), (1, 2, 3)})
print(s)
print((1, 2, 3) in s)  # Sprawdzenie istnienia w zbiorze
print((1, 4, 3) in s)  # Sprawdzenie wszystkich wartości