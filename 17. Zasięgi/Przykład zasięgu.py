# Zasięg globalny
X = 99  # X i funkcja przypisane w module: globalne
def funkcja(Y):  # Y i Z przypisane w funkcji: lokalnie
    Z = X + Y #  X jest globalne
    return Z
print(funkcja(1))  # funkcja w module: wynik 100
'''X = funkcja globalna
Y, Z = funkcja lokalna, istnieje tylko w czasei wykonaywania funkcji'''
import builtins
print(dir(builtins))
# Reguła LEGB = Local, zagnieżdżone, globalne (w module, pliku), w pythonie (builtins)