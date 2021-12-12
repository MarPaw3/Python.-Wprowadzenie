seq1 = 'mielonka'
seq2 = 'biedronka'
res = []
for x in seq1:  # dla wartości w seq1
    if x in seq2:  # jeżeli wartości należa do seq2
        res.append(x)  # wspólne wartości dodaj na końcu listy res
print(res)
# alternatywnie:
'''for x in seq1; if x in seq2:'''
