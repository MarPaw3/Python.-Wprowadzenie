rec = {'dane osobowe': {'imię': 'Robert', 'nazwisko': 'Klinek'},
       'zawód': ['mechanik', 'programista'],
       'wiek': 33 }
print(rec)  # cały słownik
print(rec['dane osobowe'], rec['wiek'])  # lub poszczególne składowe słownika
rec['zawód'].append('leśniczy')  # Dodawanie do poszczególnych kluczy dodatkowych zawartości
print(rec)  # zawartość można zmieniać (dodawać, odejmować), kluczy nie można.
