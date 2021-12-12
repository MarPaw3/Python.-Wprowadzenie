s1 = {1, 2, 3, 4}
print(s1 & {1, 3})  # Cześć wspólna & dla s1 i {1, 3}
print(s1 | {1, 5, 3, 6})  # Suma obu zbiorów |
print(s1 - {2,4})  # Różnica
print(s1 > {1, 3})  # Nadzbiór
print(s1 - {1, 2, 3, 4})  # Pusty zbiór set()
print(type({}))  # Ponieważ {} jest pustym słownikiem <class 'dict'>
S = set()  # Inicjacja pustego zbioru
print(S)
S.add(1.23)
print(S)