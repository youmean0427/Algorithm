import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    x = input().rstrip()

    if len(x) >= M:
        if x in arr:
            arr[x] += 1
        else:
            arr[x] = 1

result = sorted(arr.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for k in result:
    print(k[0])