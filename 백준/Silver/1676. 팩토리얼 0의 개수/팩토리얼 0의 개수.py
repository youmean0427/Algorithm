
N = int(input())

result = 1
for i in range (1, N+1):
    result *= i

box = list()
for i in str(result):
    box.append(i)

count = 0
for k in range(len(str(result))-1, 0, -1):
    if box[k] == '0':
        count += 1
    else:
        break


print(count)
