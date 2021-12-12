import sys
temp = sys.stdout  # Zapisanie na później
sys.stdout = open('log2.txt', 'a')  # Przekierowanie do pliku
print('mielonka')
print(1, 2, 3)
sys.stdout.close()  # Opróżnienie bufora zapisu
sys.stdout = temp  # Przywrócenie oginalnego strumienia
print('moja melonka')
print(open('log2.txt').read())  # Rezultat wcześniejszego wypisywnia