from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]

def color (arr):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = count

                while q:
                    x, y = q.popleft()

                    for n, m in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx = n + x
                        my = m + y
                        if 0 <= nx < N and 0 <= my < N:
                            if visited[nx][my] == 0:
                                if arr[nx][my] == arr[x][y]:
                                    visited[nx][my] = count
                                    q.append((nx, my))
    return count

result = color(arr)

for a in range(N):
    for b in range(N):
        if arr[a][b] == 'G':
            arr[a][b] = 'R'

print(result, color(arr))