for x in ['mielonka', 'jajka', 'szynka']:
    print(x, end=' ')  # dla każdego x wydrukuj wartość z listy

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x  # dla każdego x w liscie wydrukuj x + smu
    print(sum)  # 0 + 1 =1; 1 + 2 =3; 3 + 3 =6; 6 + 4 =10

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item
    print(prod)
