a = 12; b = {1: 'U'}
"""print(a + b)  # nie można dodawać słowników"""
a = 'mielonka'  # nie można dodawać przez append do stringów
b = [1, 2, 3]
b.append('mielonka')  # można dodawać do list przez append
print(b)
s = 'jajo'
print(s)
print(s.replace('o', 'a'))
myfile = open('myfile.txt', 'w')  # stworzenie operatora otwierającego plik myfile.txt w opcjii zapisu
myfile.write('Witaj,\nWspaniały Świecie')
myfile.close()
myfile = open('myfile.txt', 'r')
print(myfile.read())