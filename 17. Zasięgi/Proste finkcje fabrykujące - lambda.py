def maker(n):
    return lambda x: x ** n  # funkcje lambda również zapamiętuje informację o stanie
h = maker(3)
print(h(4))  # 4 ^ 3:)
