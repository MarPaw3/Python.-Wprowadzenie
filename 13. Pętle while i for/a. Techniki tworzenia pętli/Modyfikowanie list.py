L = [1, 2, 3, 4, 5]
for liczba in L:  # modyfikuję L tylko w pętli
    liczba += 1
    print(liczba, end='')
print(L)
for i in range(len(L)):
    L[i] += 1
    print(L, end=' ')