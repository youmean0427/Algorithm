import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort()
p = list(set(combinations(arr, M)))
p.sort()

for i in p:
    print(*i)

