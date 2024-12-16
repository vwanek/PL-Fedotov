# A7)

def pn(A, B):
    print(A)
    if A == B:
        return
    if A < B:
        pn(A + 1, B)
    else:
        pn(A - 1, B)
A = int(input('введите число A:'))
B = int(input('введите число B:'))
pn(A, B)

# B1)

def find_max():
    num = int(input('введите последовательность:'))
    if num == 0:
        return -1
    max1 = find_max()
    if max1 == -1:
        return num
    return max(num, max1)
maximum_value = find_max()
print("Наибольшее значение:", maximum_value)