while True:
    reply = input('wpisz dowolny tekst lub liczbę:')
    if reply == 'stop':
        print('brawo przerwałeś pętle')
        break
    try:
        num = int(reply)
    except:
        print(reply.upper())
    else:
        print(int(reply) **256 ** 2)
print('Koniec')