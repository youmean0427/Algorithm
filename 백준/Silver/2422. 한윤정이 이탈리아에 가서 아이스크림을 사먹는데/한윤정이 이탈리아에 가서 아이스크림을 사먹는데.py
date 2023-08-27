import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int,input().split())

ice = (N * (N-1) * (N-2)) // 6
comb = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    comb[a].append(b)
    comb[b].append(a)

cnt = []
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j in comb[i]:
            continue
        for k in range(j+1, N+1):
            if k in comb[i] or k in comb[j]:
                continue
            else:
                cnt.append((i, j, k))

print(len(cnt))