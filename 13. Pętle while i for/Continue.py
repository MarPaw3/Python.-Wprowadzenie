x = 10
while x:
    x -= 1
    if x % 2 != 0: continue  # nieparzyste pomijamy (jeżeli x podzielony daję resztę z dzielenia) continue
    print(x, end=' ')        # przeskocz na początek instrukcji
else: print(' ')
x = 10
while x:
    x -= 1
    if x % 2 == 0: continue  # nieparzyste są drukowane
    print(x, end=' ')
else: print('\nKonic pętli:)')

