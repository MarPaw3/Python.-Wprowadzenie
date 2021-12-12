print('%s, jajka, i %s' % ('mielonka', 'MIELONKA!'))  # Wyrażenie formatujące'
print('{:,.2f}'.format(296999.2567))  # separatory, miejscs po przecinku
print('%.2f | %+05d' % (3.141159, -42))  # Cyfry, dopełnienie, znaki
S = 'Mielonka'
print(dir(S))
print(help(S.replace))
help(str)  # help(__rodzaj_obiektu__) wyświetla wszystkie możliwe operacje na danym typie obiektu
S = 'A\nB\tC'  # "\n" oznacza znak końca wiersza, a "\t" to tabulator
print(S)
print(len(S))  # "len" każda ze składowych S to jeden znak
print(ord('\n'))  # "\n" to jeden znak zakodowany ako wartość dziesiętna 10
S = 'A\0B\0C'  # "\0", binarny bajt zerowy, nie kończy łańcucha znaków
print(S)  # można używać zarówno 'apostrofów' jak i "cudzysłowów". Obie formy są poprawne.
msg = """aaaaaaaaaaaaaaa  
bbb'''bbbbbbbbbbbbbbbbbb""bbbbbbbbbbbb'bbbbccccccccccccccccc"""  # można używać enter do przenoszenia wiadomości
print(msg)  # 
