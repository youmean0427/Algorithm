import sys
input = sys.stdin.readline

arr = [int(x) for x in input().split()]

a = []
d = []
for x in arr[0:3]:
    a.append(x * arr[3])
for y in arr[3:]:
    d.append(y * arr[0])

y = (a[2] - d[2]) / (a[1] - d[1])

if (arr[0] == 0):
    x = (arr[5] - (arr[4] * y)) / arr[3]
else:
    x = (arr[2] - (arr[1] * y)) / arr[0]

print(int(x), int(y))