items = ['aaa', 111, (4, 5), 2.01]  # Zbiór obiektów
test = [(4, 5), 3.14]  # Szukane klucze
for key in test:  # Dla wszystkich kluczy w test
    for item in items:  # dla wszystkich obiektów w items
        if item == key:  # jeżeli obiekt ma wartość klucza
            print(key, 'znaleziono')
            break
    else:
        print(key, 'nie znaleziono')
# Alternatywna wersja
for key in test:
    if key in items:
        print(key, 'znaleziono')
    else:
        print(key, 'nie znalezionon')