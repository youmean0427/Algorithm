import math

N = int(input())
arr = [int(x) for x in input().split()]
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    cnt += 1
    arr[i] = arr[i]-B

    if arr[i] > 0:
        r = arr[i] / C
        r = math.ceil(r)
        cnt += r

print(cnt)

