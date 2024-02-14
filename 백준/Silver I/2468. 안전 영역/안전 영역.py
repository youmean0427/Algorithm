import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []
max_val = 0
min_val = float('inf')

for _ in range(N):
    line = list(map(int, input().split()))
    max_val = max(max_val, max(line))
    min_val = min(min_val, min(line))
    arr.append(line)

def sink(arr, sink_num):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for n in range(len(arr)):
        for m in range(len(arr)):
            if sink_num >= arr[n][m]:
                arr[n][m] == 0
                visited[n][m] = float('inf')
            else:
                visited[n][m] = 0

    return arr, visited

def bfs(sn, sm, cnt, visited):
    q = deque([(sn, sm)])
    visited[sn][sm] = cnt
    while q:

        x, y = q.popleft()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for n, m in dir:
            nx, my = n + x, m + y
            if 0 <= nx < N and 0 <= my < N:
                if visited[nx][my] == 0:
                    visited[nx][my] = visited[x][y]
                    q.append((nx, my))

def find(arr):
    answer = 1
    for val in range(min_val, max_val + 1):
        sink_arr, visited = sink(arr, val)
        cnt = 1

        for n in range(len(arr)):
            for m in range(len(arr)):
                if visited[n][m] == 0:
                    bfs(n, m, cnt, visited)
                    cnt += 1
        answer = max(answer, cnt - 1)
    return answer

print(find(arr))