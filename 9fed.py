n = int(input('размер матрицы: '))
k = (n * n - n) // 2 + n
print(f'введите {k} элементов матрицы: ')
m = []
for i in range(n):
    m.append([0] * n)
    for j in range(i, n):
        m[i][j] = int(input('-> '))

for i in range(n):
    for j in range(i, n):
        m[j][i] = m[i][j]
for i in m:
    print(i, sep='\t')

