import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr  = [0] * (107)

for _ in range(N + M):
    x, y = map(int, input().split())
    arr[x] = y

visited = [float('inf')] * (107)
visited[1] = 0

def bfs(start):

    q = deque([start])

    while q:
        x = q.popleft()

        if x == 100:
            return

        for i in range(1, 7):
            y = x + i
            if visited[y] > visited[x] + 1:
                visited[y] = min(visited[y], visited[x] + 1)

                if arr[y]:
                    q.append(arr[y])
                    visited[arr[y]] = min(visited[arr[y]], visited[x] + 1)
                else:
                    q.append(y)

bfs(1)
print(visited[100])