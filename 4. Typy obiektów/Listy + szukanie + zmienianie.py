S = 'taczka' # łańcuch znaków
print(S)
L = list(S) # zamień na listę znaków
L[0] = 'p' # modyfikuj w miejscu 1
print(L)
Z = 'Mielonka'
print(Z.find('ie')) # znajdź ciąg znaków w obiekcie ( 1 = True )
print(Z.replace('M', 'Z')) # zamień warości w obiekcie tylko tymczasowo obiekt pozostaję bez zmian
print(S, Z)