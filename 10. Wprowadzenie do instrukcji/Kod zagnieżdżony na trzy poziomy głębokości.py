while True:
    reply = input('wpisz dowolne wartości:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print(reply.upper())
    else:
        num = int(reply)
        if num < 100:
            print('mało')
        elif num == 100:
            print('brawo trafiłeś w 100:)')
        else:
            print(num ** 2)
print('Koniec')