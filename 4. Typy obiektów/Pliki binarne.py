import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)  # tworzymy spakowane dane binarne
print(packed)  # 10 bajów to nie obiekt ani tekst
file = open('data.bin', 'wb')  # otwieramy binarny plik wyjściowy
print(file.write(packed))  # zapisujemy spakowane dane binarne
data = open('data.bin', 'rb').read()  # otwieramy i odczytujemy plik binarny
print(data)  # 10 bajtów, bez modyfikacji
data[4:8]
print(list[data])
struct.unpack('>i4sh', data)
print(data)