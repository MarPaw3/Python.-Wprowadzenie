x = 'mielonka'
y = 99
z = ['jajka']
print(x, y, z)
print(x, y, z, sep='')  # sep=''  daję możliwość edycji separatora, tutaj brak
print(x, y, z, sep=',')  # ustawienie separatora jako przecinka
print(x, y, z, end='')  # end='' ustawienie działania po wykonaniu print (domyślnie nowa linia)
# tutuj brak
print(x, y, z, sep='&&&', end='!!!\n')
print(x, y, z, sep='...', file=open('data.txt', 'w'))  # wpisanie do pliku
print(open('data.txt').read())  # wyświetleniqa pliku tekstowego