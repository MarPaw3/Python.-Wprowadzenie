f = open('script2.py')
lines = f.readline()
print(lines)
lines = [line.rstrip() for line in open('script2.py')]
print(lines)
print([line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()])  # Wydrukój listę po
# po linijce jeżeli na końcu liniji znajduję się liczba:)
