#while True:
#    print('Naciśnij kompbinację klawiszy Crtl+C, by zatrzymać!')
x = 'mielonka'
while x:  # Póki x nie jest puste
    print(x, end='...')
    x = x[1:]  # Przy każdym przejściu pętli odcinamy jeden znak z 'mielonka'
a=0; b=10
while a < b:  # jeden sposób tworzenia kodu pętli licznika
    print(a, end=' ')
    a += 1