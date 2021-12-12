print(2 **16, 2 / 5, 2/5.0, 'mielonka' + 'jajka')
s = 'szynka'
print(s + 'jajka', s * 5, s[:0])
print('zielone %s i %s' % ('jajka', s))  # znak %s jest miejscem podstawenia a po znaku % podajemy co podstawiamy
print('zielone {0} i {1}'.format('jajka', s))  # metoda podstawiania z użyciem zbiorów i metody .format
print(('x',)[0]); print(('x', 'y')[1])  # drukuje krotkę w pozycji drugiej
l = [1, 2, 3] + [4, 5, 6]
print(l, l[:], l[:0], l[-2], l[-2:])  # znaki ujemne wyznaczają początek sekwencji od tyłu
print(([1, 2, 3] + [4, 5, 6]) [2:4])  #  granica wyznaczona w przedziale jest wykluczana z sekwencji
print([l[2], l[3]])  # wydrukuj listę w pozycji trzeciej i czwartej
