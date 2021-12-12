def intersect(seq1, seq2):
    res = []  # Na początek pusta lista
    for x in seq1:  # Przeszukanie pierwszej sekwencji
        if x in seq2:  # Powtarzający się element?
            res.append(x)  # Dodanie na końcu listy wyników
    return res
s1 = 'mielonka'
s2 = 'biedronka'
print(intersect(s1, s2))  # znajdź i wydrukój wspólne litery w łańcuchach znaków

x = intersect([1, 2, 3], (2, 5))  # Działa również na różnych typach danych
print(x)
#  Wszystkie zmienne zapisane w definicji są lokalne - istniją tylko w tej funkcji