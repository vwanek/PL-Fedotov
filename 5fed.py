p = int(input())
a = 0
while p != 0:
    n = int(input())
    if n != 0 and p < n:
        a += 1
    p = n
print(a)