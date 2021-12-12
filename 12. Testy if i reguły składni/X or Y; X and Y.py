print(2 or 3, 3 or 2)  # True (operand>0) dlatego jest drukowany
print(0 or 5 or 4 or 3)  # Pierwszym prawdziwym obiektem jest 5 reszta już ie jest sprawdzana
print([] or {} or [] or ()) #?   False jest drukowaniem ostatniego obiektu

print(2 and 3, 3 and 2)  # Zwraca operand z lewej strony wyrażenia, jeżeli jest fałszem
print([] and {}) # w przeciwnym wypadku zwraca operand z prawej strony (prawda lub fałsz)
print(3 and [])  # w pythonie operacje logiczne zwracają obiekty które analizują a nie True lub False
#