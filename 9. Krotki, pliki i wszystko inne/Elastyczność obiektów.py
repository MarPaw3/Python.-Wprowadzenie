L = ['abc', [(1, 2), ([3],4)],5 ]
print(L[1][1][0][0])  # ze zbioru L poproszę grupę 2, z niej grupę 2, z niej wartość 1 a z niej wartość 1:)
X = [1, 2, 3]
L  = ['a', X, 'b']  # Osadzenie referencji do zmiennej X
D = {'x' : X, 'y' : 2}
X[1] = 'niespodzianka'
print(L); print(D); print(X)
L = [1, 2, 3]; D = {'a' : 1, 'b' : 2}
A = L[:]  # A jest kopią listy L
B = D.copy()  # B jest koią słownika D
A[1] = 'Ni'; B['c'] = 'mielonka'
print(A, B)
X = [1, 2, 3]; L = ['a', X[:], 'b']; D = {'x' : X[:], 'y' : 2}
X[1] = 'mielonka'; print(X, D, L)
import copy
X = copy.deepcopy(X)  # Pełna kopia dowolnie zagnieżdżonego obiektu X
print(X)