def times(x, y):  # Utworzenie i przypisanie funkcji
    return x * y  # ciało funkcji wykonywane po wywołaniu
print(times(2, 4))  # wywołanie funkcji
print(times('Ni', 16))  # Dla funkcji typ nie ma znaczenia
def intersect(seq1, seq2):
    res = []  # Na początek pusta lista
    for x in seq1:  # Przeszukanie pierwszej sekwencji
        if x in seq2:  # Powtarzający się element?
            res.append(x)  # Dodanie na końcu listy wyników
    return res
print(intersect('tuńczyk', 'mielonka'))
