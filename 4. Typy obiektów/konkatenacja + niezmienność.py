# łączenie dwóch łańcuchów znaków w jeden ciąg
s = 'Mielonka'
print(s)
s + 'kechup'
print(s)
print(s + ' + ketchup')
# Niezmienność - łańcuchy w Pythonie są niezmienne (immutable)
# s[0] = 'z' # błąd! odznaczony #
print(s)
s = 'Z' + s[1:]
print(s) # można stworzyć wyrażenie budując nowy obiekt