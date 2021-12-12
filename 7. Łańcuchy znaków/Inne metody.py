line = "Rycerze, którzy mówią Ni! \n"
print(line.rstrip())
print(line)
print(line.find('Ni') != -1)  # Szukanie za pomocą wywołania metody lub wyrażenia
print('Ni' in line)
sub = 'Ni! \n'
print(line.endswith(sub))  # Sprawdzenie końca łańcucha za pomocą wywołania mwtody lub wycinka
print(line[-len(sub):] == sub)
