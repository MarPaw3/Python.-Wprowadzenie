def func():
    x = 4
    action = (lambda n: x ** n)  # x pamiętane z zasięgu zawierającego instrukcje def
    return action
x = func()
print(x( 2))