x = 2
y = 4
z = 6
print(x<y<z)  # Połączone porównania - testy przedziału
print(x<y and y<z)
print(1.1 + 2.2 == 3.3)  # nie jest równe ze względu na prblem precyzji liczb
print(1.1 + 2.2)  # wynik to 3.3000...003
print(int(1.1 + 2.2) == int(3.3))  # wynik poprawny po konwersji do intiger'ów
# nie możemy odwzorować za pomocą ograniczonej ilości bitów liczb zmiennoprzecinkowych!!!
print(4 / 3)
print( 4 // 3)  # dzielenie bez reszty