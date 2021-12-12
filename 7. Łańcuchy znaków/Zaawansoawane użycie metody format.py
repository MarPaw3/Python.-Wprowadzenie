print('{0:10} = {1:10}'.format('jajko', 123.4567))
print('{:>10} = {:<10}'.format('jajko', 123.4567))
print('{name} {job} {name}'.format(name='Adam', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Adam', job='dev'))
D = dict(name='Adam', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))  # Metoda format; odwołania do kluczy słownika
