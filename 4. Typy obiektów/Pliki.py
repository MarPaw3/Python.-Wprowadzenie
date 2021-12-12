f = open('data.txt', 'w')  # utworzenie nowego pliku w trybie do zapisu
f.write('Witaj,\n')  # Zapisanie ciągu znaków w pliku ("\n" zaczyna od nowej linijki tekstu)
f.write('Brian\n')
f.close()  # zapisanie bufora wyjściowego na dysku i zamknięcie pliku
f = open('data.txt')  # tryb do odczytu ('r') jest domyślym trybem przetwarzania plików
text = f.read()  # załadownie całego pliku do obiektu testowego
print(text)  # drukuje zawartość pliku
print(text.split())  # zawartość pliku jest zawsze łańcuchem znaków
print(dir(f))  # pokazuje wszystkie dostępne metody dla pliku
print(help(f.seek))  # funkcja help dla konkretnej metody pokazuję jej opis