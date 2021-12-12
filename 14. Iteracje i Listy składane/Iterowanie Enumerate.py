e = enumerate('spam')  # Wynik funkcji enumerate() również jest obiektem iterowalnym
print(e)
i = iter(e)
print(next(i))  # Wygenerowanie wyników z użyciem protokołu iteracyjnego
print(next(i))  # Wygenerowanie wyników z użyciem protokołu iteracyjnego
print(next(i))  # Wygenerowanie wyników z użyciem protokołu iteracyjnego
print(next(i))  # Wygenerowanie wyników z użyciem protokołu iteracyjnego
print(list(enumerate('spam')))  # Przekszatłcenie na listę generującą wszystkie elementy jednocześnie