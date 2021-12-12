#  po lewej stronie operatora % umieszczamy łańcuch znaków który będzie formatowany
#  po prawej stronie operatora % umieszczamy obiekt w krotce który ma być wstawiony w miejsce
print('Ten %d %s jest martwy!' %(1, 'ptak'))
exclamation = 'Ni'
print('Rycyerze, którzy mówią %s !' % exclamation)  # podstawienie łańcucha znaków
print('%d %s %d you' % (1, 'spam', 4))  # Podstawienie zależne od typu %d = wstaw liczbę dziesiętną
print('%s--%s__%s' % (42, 3.14159, [1, 2, 3]))  # Wszystkie typy pasują do znacznika %s=(wstaw string)
print('Jeden %s %d' % ('z', 10))  # %s wstaw string, %d wstaw liczbę dziesiętną

