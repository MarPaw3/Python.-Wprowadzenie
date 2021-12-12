x, y, z = 43, 44, 45
s = 'Mielonka'
d = {'a' : 1, 'b' : 2}
l = [1, 2, 3]
f = open('datafile.txt', 'w')  # Utworzenie wyjścioweo pliku tekstowego
f.write(s + '\n')  # zakończenie wierszy znakiem \n
f.write('%s, %s, %s\n' % (x, y, z))
f.write(str(l) + '$' + str(d) + '\n')  # Konwersja rozdzielenia znakiem $
f.close()
chars = open('datafile.txt').read()  # 
print(chars)