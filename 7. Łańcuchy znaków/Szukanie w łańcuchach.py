s = 'xxxxjajkaxxxxjajkaxxxx'
print(s.replace('jajka', 'mielonka'))  # zastępuje wszystkie wyrażenia
print(s)
print(s.replace('jajka', 'mielonke', 1))  # zastępuje jedno wystąpienie
print(s)  # łańcuch pozostaję niezmieniony
s = list(s)  # przekształcenie łańcucha na listę ułatwia jego modyfikowanie
print(s)
s = 'brama'
s = list(s)
print(s)
s[2] = 'e'
s[3] = 'j'
print(s)
s = ''.join(s)  # funkcja przekształcenia listy w stringi
print(s)
print('JAJKA'.join(['mielonka', 'ser', 'szynka', 'tost']))  # .join łączy wszystko do stringa