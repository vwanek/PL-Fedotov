s = input('Введите строку')
s1 = s[:int((len(s) + 1) / 2)]
s2 = s[int((len(s) + 1) / 2):]
r = ''
for i in s1:
    if i == 'п' or i == "П":
        r += '*'
    else:
        r += i
r += s2
print(r)