'''afile = open(nazwa_pliku, tryb_przetwarzania
afile.metoda()'''
myfile = open('myfile.txt', 'w')  # Otwarcie do zapisu tekstowego (tworzy pusty plik)
myfile.write('Witaj, pliku tekstowy\n')  # zapisanie wiersza tekstu
myfile.write('Żegnaj, pliku tekstowy\n')
myfile.close()  #Zrzucenie bufora wyjściowego na dysk
myfile = open('myfile.txt')  # Otwarcie do odczytu tekstu- 'r' jest domyślne
print(myfile.readline())  # wczytanie wierszy z powrotem
print(myfile.readline())  # wczytanie kolejnego wiersza
print(myfile.readline())  # pusty łańcuch znaków - koniec pliku
print(open('myfile.txt').read())  # wczytanie wszystkiego naraz do łańcucha znaków

