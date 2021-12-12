x = 99
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()
print(f1(), x)
def f1():
    x = 88
    def f2():
        print(x)  # Pamięta x w zasięgu fukcji zawierającej
    return f2()  # Zwraca funkcję f2, alę jej nie wywołuje
action = f1()  # Utworzenie i zwrócenie funkcji
print(action)