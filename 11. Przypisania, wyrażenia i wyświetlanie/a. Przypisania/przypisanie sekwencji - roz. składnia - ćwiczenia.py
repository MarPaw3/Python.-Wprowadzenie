a, *b = 'spam'
print(a, b)
a, *b, c = 'spam'
print(a, b, c)
S = 'spam'
print(S[0], S[1:])
L = [1, 2, 3, 4]
while L:
    front, *L = L  # pobieramy element i listę pozostałych, bez wycinania
    print(front, L)
