S = input()

# print(S)

a = list()
b = list()

for i in 'KOREA':
    if i in S and i not in a:
        a.append(i)


for i in 'YONSEI':
    if i in S and i not in b:
        b.append(i)


if ''.join(a) == 'KOREA':
    print(''.join(a))
else:
    print(''.join(b))
