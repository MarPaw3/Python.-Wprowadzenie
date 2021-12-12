seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
'''a, b = seq  # przypisanie nie jest możliwe jeżeli ilość elementów po obu stronach się nie zgadza'''
a, *b = seq
print(a, b)  # gwiazdka * powoduje że do elementu z gwaizdką są przypisywane wszytkie pozostałe elementy
*a , b = seq
print(a, b)  # miejsce wystąpienia gwiazdki determinuje kierunek przypisania pozostałych elementów
a, *b, c = seq
print(a, b, c)  # do elementu z gwiazdką zostaną przypisane wszystkie elementy do których nie ma bezpośredniego
# przypisania
