import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [0] * (101)

for _ in range(N + M):
    x, y = map(int, input().split())
    arr[x] = y

visited = [float('inf')] * (101)
visited[1] = 0
visited[0] = 0

def bfs(start):

    q = deque([start])

    while q:

        x = q.popleft()

        if x == 100:
            return

        for i in range(1, 7):
            y = x + i
            if 0 <= y <= 100 and visited[y] > visited[x] + 1:
                if arr[y]:
                    if visited[arr[y]] > visited[x] + 1:
                        visited[arr[y]] = visited[x] + 1
                        q.append(arr[y])
                else:
                    visited[y] = visited[x] + 1
                    q.append(y)

bfs(1)
print(visited[100])