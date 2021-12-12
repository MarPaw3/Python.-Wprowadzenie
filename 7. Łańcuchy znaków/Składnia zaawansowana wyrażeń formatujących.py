#  %[(nazwa)][opcje][szerokość][.precyzja]kod_typu
x = 1234
res = 'integers: ...%d...%-6d...%06d'% (x, x, x)
print(res)
print('%(ilość)d%(towar)s'% {'ilość':1, 'towar':'mielonka'})
#  Szablon ze znacznikami podstawienia
reply = '''Witamy...\nWitaj %(name)s!\nTwój wiek to %(age)s lat.'''
valves = {'name':'Amadeusz', 'age':40}
print(reply % valves)
food = 'mielonka'
qty = 10
print(vars())
print('%(qty)d razy %(food)s' %vars())