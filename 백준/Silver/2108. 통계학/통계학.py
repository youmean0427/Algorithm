import sys
input=sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    a = int(input())
    arr.append(a)

# print(arr)

avg = sum(arr) / len(arr)
print(round(avg))

arr = sorted(arr)
print(arr[N//2])

count = {}

for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

count = sorted(count.items(), key=lambda item: item[1], reverse=True, )
top = count[0][1]
del_count = 0
for i in range(len(count)):
    if count[i][1] < top:
        del_count += 1

for k in range(del_count):
    count.pop(-1)

if len(count) >= 2:
    print(count[1][0])
else:
    print(count[0][0])

print(arr[-1] - arr[0])