x, y = 'mielonka', 'MIELONKA'
x = x + y
print(x, y)
x += y  # ten sam rodzaj przypisania jak wyżej ale w krótszej formie
print(x, y)
a, b = 2, 4
a *= b  # przypisanie z pomnożeniem przez b
print(a)
l = [1, 2, 3, 4]
l.append(5)  # dodaję w miejscu  ' append = wstaw
l.extend([6, 7])  # dodaję na końcu ' extend ' wstaw na końcu
print(l)
# konkatencja l = l + [5]; l = l + [6, 7] działa wolniej.
l += [8, 9, 10]  # Odwzorowanie na l.extend([8, 9, 10]}
print(l)
l = []
l += 'jelonka'  # += oraz extend zezwalają na użycie dowolnej sekwencji, ale z operatorem + tak nie jest!
print(l)