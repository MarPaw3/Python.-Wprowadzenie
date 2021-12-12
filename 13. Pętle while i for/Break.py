while True:
    name = input('Podaj imię:')
    if name == 'stop': break
    age = input('Podaj wiek:')
    print('Witaj,', name, '=> Kwadrat Twojego wieku to:', int(age) **2)
