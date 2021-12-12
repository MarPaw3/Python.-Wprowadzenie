from fractions import Fraction
x = Fraction(1, 3)  # 1 - licznik, 3 - mianownik
print(x)
y = Fraction(4, 6)
print(y)
print(Fraction(x, y))
print(Fraction(0.25))  # można utworzyć ułamek zwykły z ułamka dziesiętnego
print(Fraction(1.3))  # :)))
print(2.5.as_integer_ratio())
f = 2.5
z = Fraction(*f.as_integer_ratio())  # Konwersja z liczby zmiennoprzecinkowej na ułamek: 2 argumenty
print(x + z)  # 5/2 + 1/3 = 15/6 + 2/6
print(float(x))
print(Fraction.from_float(1.75))  # Konwersja z liczby zmiennoprzecinkowej na ułamek: inny sposób
print(Fraction(*1.75.as_integer_ratio()))