d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d.keys():
    print(key, d[key])
import os
p = os.popen('dir')
print(p.__next__())
print(p.__next__())
print(p.__next__())