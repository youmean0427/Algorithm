import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement as cr

N, M = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()
result = []
def dfs(n, sm):

    if len(sm) >= M:
        print(*sm)
        return

    for i in range(n, N):
        dfs(i, sm + [arr[i]])

dfs(0, [])
