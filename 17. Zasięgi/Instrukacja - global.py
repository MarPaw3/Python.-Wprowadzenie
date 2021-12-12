x = 88  # Zmienna globalna x
def func():
    global x
    x = 99
      # Zmiana x poza def (global)
func()  # Dopiero użycie funkcji z definicji zmieni wartość globalnie
print(x)
y, z = 1, 2  # deklaracja ziennych globalnie
def all_global():
    global x    # deklaracja obiektu globalnie w definicji
    x = y + z   # utworzenie obiektu w definicji
all_global()
print(x)