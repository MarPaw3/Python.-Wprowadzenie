print('Ni!' * 4)
print('mielonka\n' * 24 ** 2)
myjob = 'haker'
for c in myjob:
    print(c, end='')  # Przechodzenie przez kolejne elementy i wyświetlanie ich
print('k' in myjob)  # sprawdzenie czy jest k
print('z' in myjob)  # sprawdzenie czy jest z
print('jajko' in 'adszjajkopkkmm')  # Wyszukiwanie podciągu znaków, pozycja nie jest zwracana
s = 'mielonka'
print(s[0], s[1:3], s[2:], s[:-2])  # Znak : jest granicą zapytnia = :-2 od początku do 2 pozycji od końca
print(s[::2])  # pierwszy : to wartość przedziału a drugi : daję wartość kroku pominięcia
print(s[::-1])  # krok ujemny daję możliwość odczytu stringu od tyłu
print(s[4:2:-1])

