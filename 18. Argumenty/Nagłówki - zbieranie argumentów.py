def f(*args): print(args)  # Stworzenie funkcji z dowolną ilością argumentów
print(f())
print(f(1))
print(f(1, 2, 3, 4, 5,))
def f(**args): print(args)  # Stworzenie funkcji z dow... zamienianą na słówniki
print(f(a=1, b=5))
def func(a, b, c, d): print(a, b, c, d)
args = {'a':1, 'b':2, 'c':3}
args['d'] = 4
print(func(**args))
