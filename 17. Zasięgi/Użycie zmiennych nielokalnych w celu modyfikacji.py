def tester(start):
    state = start  # Każde wywołanie otrzymuje własną zmienną state
    def nested(lebel):
        nonlocal state  # Pamięta state z zasięgu funkcji zawierającej
        print(lebel, state)  # Można zmienić jeżeli posiada argument nonlocal
        state += 1
    return nested
F = tester(0)
print(F('szynka'))  # Inkrementuje state z każdym wywołaniem
print(F('mielonka'))
print(F('jajko'))
G = tester(42)  # Utwozenie nowej funkcji tester rozpoczynającej się od 42
print(G('bób'))
print(G('miód'))
print(F('tlen'))  # Dla F pozostają tskie same