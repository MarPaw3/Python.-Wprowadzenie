print({x ** 2 for x in [1, 2, 3, 4]})  # Utwórz nowy zbiór dla x do kwadratu dla każdego x z listy
print({x for x in 'mielonka'})  # To samo co set('mielonka')
print({c * 4 for c in 'mielonka'})  # Zbiór zebranych wyników wyrażenia
print({c * 4 for c in 'szynkajajka'})
s = {c * 4 for c in 'mielonka'}
print(s | {'mmmm', 'xxxx'})
print(s & {'mmmm', 'xxxx'})