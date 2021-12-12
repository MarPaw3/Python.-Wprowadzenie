adam = ('Adam', 40.5, ['dev', 'mgr'])  # rekord w postaci krotki
print(adam)
print(adam[0], adam[2])  # Dostęp do pól według pozycji w krotce
from collections import namedtuple  # import typu rozszerzonego
rec = namedtuple('rec', ['name', 'age', 'jobs'])  # utworzenie instancji klasy
adam = rec('Adam', age=40.5, jobs=['dev', 'mgr'])
print(adam.name, adam.jobs)  # dostęp według atrybutów
O = adam._asdict()  # Rekord w postaci zbliżonej do słownika
print(O)