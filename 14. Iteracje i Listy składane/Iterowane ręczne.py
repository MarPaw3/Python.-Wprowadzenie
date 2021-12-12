l = [1, 2, 3]
for x in l:  # Iteracja automayczna
    print(x ** 2, end='')  # Wywołuje funkcje iter(), metodę __next__, przechwytuje wyjątki
i = iter(l)  # ręcza iteracja: pętla for robi to samo nie jawnie
while True:
    try:
        x = next(i)
    except StopIteration:
        break
    print(x ** 2, end='')

