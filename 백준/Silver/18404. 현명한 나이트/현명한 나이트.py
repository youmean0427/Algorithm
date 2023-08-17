import sys
input = sys.stdin.readline

N, M = map(int, input().split())

x, y = map(int, input().split())
x, y = x - 1, y - 1

board = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[x][y] = 0

q = [(x, y)]

while q:

    n, m = q.pop(0)
    dire = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    for i, j in dire:
        ni = n + i
        mj = m + j

        if 0 <= ni < N and 0 <= mj < N:
            if visited[ni][mj] == 0:
                visited[ni][mj] += visited[n][m] + 1
                q.append((ni, mj))

result = []
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    result.append(visited[a][b])

print(*result)
