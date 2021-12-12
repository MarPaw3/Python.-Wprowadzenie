def tester(start):
    state = start  # Referencja do zmiennej nielokalnej działa normalnie
    def nested(label):
        print(label, state)  # Pamięta stan w zasięgu funkcji zawierającej
    return nested
F = tester(0)
print(F('mielonka'))
print(F('szynka'))