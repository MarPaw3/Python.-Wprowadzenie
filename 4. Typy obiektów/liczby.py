import decimal
from fractions import Fraction  # Ułamki - licznik i mianownik

print(1 / 3)  # Liczby zmiennoprzecinkowe
print(2 / 3 + 1 / 2)
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
print(1 > 2, 1 < 2)  # Warości typu Boolean
print(bool('mielonka'))  # Wartość logiczna obiektu:)
X = None  # Obiekt None
print(X)
L = [None] * 100  # Zainicjowanie listy stu obiektów None
print(L)
