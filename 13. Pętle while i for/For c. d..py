S = 'drwal'
T = ('i', 'jestem', 'git')
for x in S:
    print(x, end=' ')  # iterowanie po łańcuchu znaków
else: print('')
for x in T: print(x, end='\n')

t = [(1, 2), (3, 4), (5, 6)]
for (a, b) in t:  # przypisanie krotek do a i b
    print(a, b)