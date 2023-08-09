import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            q = deque([(i, j)])
            break

while q:
    x, y = q.popleft()

    for n, m in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = n + x
        my = m + y
        if 0 <= nx < N and 0 <= my < M:
            if visited[nx][my] == 0 and arr[nx][my] == 1:
                q.append((nx, my))
                visited[nx][my] = visited[x][y] + 1

for a in range(N):
    for b in range(M):
        if visited[a][b] == 0 and arr[a][b] == 1:
            visited[a][b] = -1
        print(visited[a][b], end=' ')
    print()
