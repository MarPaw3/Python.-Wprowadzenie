string = 'jajo'
a, b, c, d = string  # Ta sama liczba elementów po obu stronach musi BYć!
print(a, d)
'''a, b, c = 'jajko'  # błąd'''
a, b, c, = string[0], string[1], string[2:]
print(a, b, c)
(a, b), c = string[:2], string[2:]  # wersja z zagnieżdżonymi sekwencjami
print(a, b, c)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:...  # Proste pzypisanie do krotki
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:...  # Zagnieżdżone przypisanie krotki
print(list(range(3)))  # list jest wymagane dla przedstawienia range
