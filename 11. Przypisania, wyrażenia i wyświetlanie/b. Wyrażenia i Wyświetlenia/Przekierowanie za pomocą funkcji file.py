log = open('log.txt', 'a')
print('x', 'y', 'z', file=log)  # Zapis do pliku
print('a', 'b', 'c')  # Zapis do orginalnego strumienia stdout
