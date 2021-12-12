template = '{0}, {1} i {2}'  # Podstawienie pozycyjne
print(template.format('Tytus', 'Romek', 'Atomek'))
template = '{pieczywo}, {wędlina} i {nabiał}'
print(template.format(pieczywo='chleb', wędlina='mielonka', nabiał='jajka'))
template = '{}, {} i {}'
print(template.format('indyk', 'indoor', 'outdoor'))  # Podstawienie przez pozycję bezwzględną
import sys
print('Mój {1[spam]} ma zainstalowany system {0.platform}'.format(sys, {'spam': 'laptop'}))
somelist = list('jajko')
print(somelist)
print('pierwszy={0[0]}, trzeci={0[2]}'.format(somelist))