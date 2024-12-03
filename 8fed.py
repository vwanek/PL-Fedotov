# 1)

import math

x = float(input('введите x'))
y = float(input('введите y'))
z = float(input('введите z'))
t = float(input('введите t'))
diag = math.sqrt(x*x + y*y)

def kv4 (x,y):
    return x * y * 0.5

def kv3 (diag, z, t):
    p = (z + t + diag) / 2
    return math.sqrt(p * (p - z) * (p - t) * (p - diag))
print(kv4(x, y) + kv3(diag, z, t))


# 2)

def oct(n):
    m = ""
    while n != 0:
        m = str(n%8) + m
        n //= 8
    return "{0:0>10}".format(m)
a = int(input('введите число'))
print(oct(a))
