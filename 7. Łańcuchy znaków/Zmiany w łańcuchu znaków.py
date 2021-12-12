S = 'mielonka'
S = S + 'MIELONKA!'
print(S)
S = S[:8] + 'jajka' + S[-1]  #  Dodajemy 'jajka' i znak !
print(S)
S = S.replace('lon', 'lonecz')  # funkcja replace zastępuje wybrany fragment stringa
print(S)
print('Ten %d %s jest martwy!' %(1, 'ptak'))  # Wyrażenie formatujące
print('Ten {0} {1} jest martwy!'.format(1, 'ptak'))  # Metoda formatjąca
