import sys
input = sys.stdin.readline
from itertools import combinations
N, L, R, X = map(int, input().split())
arr = [int(x) for x in input().split()]
result = []
for i in range(N+1):
    q = list(combinations(arr, i))
    # print(q)

    for k in q:
        if k:
            if max(k) - min(k) >= X:
                if L <= sum(k) <= R:
                    result.append(k)

print(len(result))