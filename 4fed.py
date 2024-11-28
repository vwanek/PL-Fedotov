n = int(input())
s = 1
k = 1
for i in range(2, n + 1):
    k *= i
    s += k
print(s)