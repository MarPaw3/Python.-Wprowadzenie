import pickle
d = {'a' : 1, 'b' : 2}
f = open('datafile.pkl', 'wb')
pickle.dump(d, f)  # Serializacja dowolnego obiektu w pliku
f.close()
f = open('datafile.pkl', 'rb')
e = pickle.load(f)  # załadowanie dowolnego obiektu z pliku
print(e)