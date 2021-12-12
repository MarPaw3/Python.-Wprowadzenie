f = open('script2.py')
print(f.__next__())  # Bezpśrednie wywołanie iteratora
print(f.__next__())  # Bezpśrednie wywołanie iteratora kolejnej linii
print(next(f))
l = [1, 2, 3]
i = iter(l)  # Pozyskanie obiektu iteratora z obiektu iterowalnego
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())  # komunikat o błędzie z powodu StopIteration

