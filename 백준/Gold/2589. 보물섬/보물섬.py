import sys
input = sys.stdin.readline
from collections import deque

def bfs(arr, start):

    q = deque([start])
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    distance = []
    while q:

        x, y = q.popleft()

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for n, m in dir:
            nx = n + x
            my = m + y

            if 0 <= nx < N and 0 <= my < M:
                if arr[nx][my] == "L" and visited[nx][my] == 0:
                    visited[nx][my] = visited[x][y] + 1
                    distance.append(visited[nx][my]-1)
                    q.append((nx, my))
    return distance

N, M = map(int, input().split())
map = [[x for x in input().rstrip()] for _ in range(N)]
result = 0

for a in range(N):
    for b in range(M):
        if map[a][b] == "L":
            distance_list = bfs(map, (a, b))
            if distance_list:
                result = max(result, max(distance_list))

print(result)