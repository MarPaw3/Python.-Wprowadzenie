y = input('podaj liczbę:')
x = int(y) // 2
while x > 1:
    if int(y) % x == 0:
        print(y, 'ma czynnik', x)
        break
    x -= 1
else:
    print(y, 'jest liczbą pierwszą')