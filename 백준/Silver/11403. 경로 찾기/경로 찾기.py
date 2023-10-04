import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

def dfs(arr, start):

    visited = [0] * N
    q = deque([start])

    while q:

        x = q.pop()

        for k in range(N):
            if arr[x][k] == 1 and visited[k] == 0:
                visited[k] = 1
                q.append(k)

    return visited

for i in range(N):

    result = dfs(arr,i)
    print(*result)