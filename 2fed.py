import math
x = float(input('Введите переменную x:'))
y = float(input('Введите переменную y:'))
z = float(input('Введите переменную z:'))
s = (abs(math.cos(x) - math.cos(y)))**(1 + 2 * math.sin(y)**2) * (1 + z + z**2/2 + z**3/3 + z**4/4)
print(s)