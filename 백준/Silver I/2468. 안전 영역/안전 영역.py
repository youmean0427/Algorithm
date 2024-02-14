import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

def sink(arr, sink_num):
    visited = [[0] * N for _ in range(N)]

    for n in range(N):
        for m in range(N):
            if arr[n][m] <= sink_num:
                arr[n][m] = 0
                visited[n][m] = 1

    return visited

def bfs(sn, sm, visited):
    q = deque([(sn, sm)])
    visited[sn][sm] = 1
    while q:
        x, y = q.popleft()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for n, m in dir:
            nx, my = n + x, m + y
            if 0 <= nx < N and 0 <= my < N and not visited[nx][my]:
                visited[nx][my] = 1
                q.append((nx, my))

def find(arr):
    answer = 1
    for val in range(1, 101):
        visited = sink(arr, val)
        cnt = 0

        for n in range(N):
            for m in range(N):
                if not visited[n][m]:
                    bfs(n, m, visited)
                    cnt += 1
        answer = max(answer, cnt)
    return answer

print(find(arr))
