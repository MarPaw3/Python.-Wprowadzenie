L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))  # Przekształcenie listy w zbiór, usunięcie duplikatów.
L = list(set(L))  # Przekształcenie zbioru z powrotem na listę.
print(L)
print(list(set(['yy', 'xx', 'ee', 'qq'])))  # kolejność nie zostanie zachowana
print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))  # Wyszukiwanie różnic w listach
print(set('abcdefg') - set('abdghij'))  # Wyszukiwanie różnic w ciągach znaków
print(set('spam') - set(['h', 'a', 'm']))  # -||- -||-, tryb mieszany
print(set(dir(bytes)) - set(dir(bytearray)))  # Różnica atrybutów między typem bytes a bytearray
print(set(dir(bytearray)) - set(dir(bytes)))  # Różnica ...
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 ==L2)  # Kolejność elementów w sekwencjach ma znaczenie
print(set(L1) == set(L2))  # Testowanie równości niezależne od kolejności elementów
print(sorted(L1) == sorted(L2))  # Podobne działanie ale wyniki są posortowane
print('spam' == 'asmp', set('spam') == set('asmp'))  