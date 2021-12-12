open('script2.py').read()
print(open('script2.py').read())
f = open('script2.py')  # odczytanie 4 - wierszowego skryptu  bieżącego katalogu
print(f.readline()) # fukcja readline wczytuję po jednym wierszu
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
for line in open('script2.py'):  # Użycie iteratora do odczytywania pliku wiersz po wierszu
    print(line.upper(), end='')  # Wywołuje __next__, przechwyuje StopIteration
# Najlepsza metoda odczytywania pliku wiersz po wierszu
