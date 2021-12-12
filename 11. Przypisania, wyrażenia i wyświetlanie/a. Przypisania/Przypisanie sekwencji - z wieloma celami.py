a = b = c = 'mielonka'
print(a, b, c)
a = b = 0  # w przypadku typów niemutowalnych należy najpierw przypisać jakąś wartość
b = b + 1
print(a, b)
a = b = []
b.append(42)  # przypisanie do jednej powoduję zmianę drugiego obiektu ze względu na współdzielenie miejsca
print(a, b)
a = []
b = []
b.append(18)
print(a, b)
# lub
a, b = [], []
print(a, b)