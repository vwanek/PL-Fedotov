from random import *

n = [randint(0,10) for i in range(8)]
s = 0
p = 1
print(n)
for i in range(len(n)):
    if i % 2 == 0:
        s += n[i]
    else:
        p *= n[i]
print(s, p)