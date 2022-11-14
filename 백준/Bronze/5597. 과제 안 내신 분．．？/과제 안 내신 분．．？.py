result = []
for i in range(28):
    result.append(int(input()))
for i in range(1, 31):
    if i not in result:
        print(i)