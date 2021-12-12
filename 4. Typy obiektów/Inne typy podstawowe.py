#  Sety = zbiory
from typing import List

X = set('mielonka')  # utworzenie zbioru z sekwencjami.
Y = {'s', 'z', 'y', 'n', 'k', 'a'}  # utworzenie zbioru za pomocą literału
print(X, Y)  # krotka z dwóch zbiorów bez nawiasów
print(X & Y)  # część wspólna zbiorów
print( X | Y)  # suma zbiorów
print(X - Y)  # różnica zbiorów
print(X > Y)  # Nadzbiór
print({x ** 2 for x in [1, 2, 3, 4]})  # zbiory składane
print(list(set([1, 2, 1, 3, 1])))  # Filtrowanie duplikatów (elementy nie muszą być uporządkowane)
print(set('mielonka') - set('szynka'))  # Wyszukiwanie różnic w kolejkach
print(set('mielonka') == set('alkmoeni'))  # Test równości niezależny od kolejności elementów
print('n' in set('mielonka'), 'n' in 'mielonka', 'szynka' in ['jajka', 'mielonka', 'szynka'])