print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
# piewsza wartość wyznacza ilość od zera licząc, druga wartość wyznacza górną granicę listy
# trzecia wartość wyznacza o jaki krok tworzyć listę
print(list(range(-5, 9, 2)), list(range(5, -12)))
# jeżeli lista ma być tworzona od + do - jej krok musi być ujemny
for ł in range(3):
    print(ł, 'Python')
x = 'mielonka'
for litera in x: print(litera, end=' ')  # prosta iteracja
i = 0 ;print('')  # lub metoda z while
while i < len(x):
    print(x[i], end=' ')
    i +=1  #  # lub najprościej
for i in x: print(i, end=''); x = 'abcdefghij'
for i in x[::2]: print(i, end=' ')  #co druga wartość