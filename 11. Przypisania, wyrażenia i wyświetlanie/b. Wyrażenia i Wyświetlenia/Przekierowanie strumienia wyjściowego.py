x, y, z = 'Witaj', 'Świecie', '!!!'
import sys
sys.stdout = open('log.txt', 'a')  # przekierowanie print do pliku
print(x, y, x)  # wykonanie przekierowwania przez funkcje print
temp = sys.stdout  # zapisanie w temp

