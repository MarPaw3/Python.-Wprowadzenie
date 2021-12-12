class Worker:
    def __init__(self, name, pay):  # Inicjalizacja przy utworzeniu
        self.name = name  # self jest nowym obiektem; name to nazwisko, a pay - płaca
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]  # Podział łańcucha na pustych znakach

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Uaktualnienie płacy w miejscu

bob = Worker('Robert Zielony', 40000)
anna = Worker('Anna Czerwona', 50000)

print(bob.lastname())
anna.giveRaise(.10)  # uaktualnienie płacy anny
print(int(anna.pay))  # w liczbach całkowitych
