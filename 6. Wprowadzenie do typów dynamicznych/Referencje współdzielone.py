L1 = [2, 3, 4]
L2 = L1
L1[0] = 24  # lista L1 się zmienia w miejscu [0]
print(L2)  # Tak samo lista L2
print(L1)
L1 = [2, 3, 4]
L2 = L1[:]  # Utworzenie kopii L1 (lub listy(L1), copy.copy(L1) itp.
L1[0] = 24
print(L1)
print(L2)  # L2 nie zmienia się
Y = 'mielonka'
import copy
X = copy.copy(Y)  # Wykonanie płytkiej kopii dowolnego obiektu Y
X = copy.deepcopy(Y)  # Wykonanie kopii wszystkich elementów zagnieżdżonych w Y
L = [1, 2, 3]
M = L
print(L==M)  # Porównaj wartości obiektów
print(L is M)  # Porównaj identyczność obiektów (mocniejsza forma sprawdzenia)
L = [1, 2, 3]
M = [1, 2, 3]
print(M is L)  # Są to różne obiekty o tych samych wartościach ( False )
# ale
x = 42
y = 42
print(x is y)  #  42 jest jednym obiektem przechowywanym w pamięci podręcznej
import sys
print(sys.getrefcount(1))  # ilość odniesień do wartości 1 w pamięci
print(sys.getrefcount(42))
