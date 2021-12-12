engineers = {'Robert', 'Amadeusz', 'Anna', 'Aleksander'}
managers = {'Edward', 'Amadeusz'}
print('Robert' in engineers)  #  Czy Robert jest inżynierem?
print(engineers & managers)  # Kto jest inżynierem i menadżerem?
print(engineers | managers)  # Wszystkie osoby z obu kategorii
print(engineers - managers)  # Inżynierowie którzy nie są menadżerami
print(engineers > managers)  # Czy menadżerowie są inżynierami? (nadzbiór)
print({'Robert', 'Amadeusz'} < engineers)  # Czy obaj są inżynierami
print((managers | engineers) > managers)  # Nadzbiorem menadżerów są wszyscy pracownicy
print(managers ^ engineers)  # Kto jest w jednym zbiorze, ale nie w obu?
print((managers | engineers) - (managers ^ engineers))  # Część wspólna