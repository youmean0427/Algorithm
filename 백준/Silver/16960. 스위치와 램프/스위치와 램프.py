import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(1, N+1):
    info = [int(x) for x in input().split()]

    for j in info[1:]:
        arr[i].append(j)

a = list(combinations(arr[1:], N-1))

for i in a:
    lamps = [0] * (M + 1)
    for j in i:
        for k in j:
            lamps[k] = 1

    if lamps.count(1) == M:
        result = 1
        print(result)
        exit(0)

print(0)