import sys, copy
from itertools import combinations
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
zero = []
virus = []
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(len(line)):
        if line[j] == 0:
            zero.append((i, j))
        if line[j] == 2:
            virus.append((i, j))

def bfs(sn, sm):

    q = [(sn, sm)]
    visited[sn][sm] = 2
    while q:
        x, y = q.pop(0)

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for n, m in dir:
            nx = n + x
            ym = y + m
            if 0 <= nx < N and 0 <= ym < M:
                if visited[nx][ym] == 0:
                    visited[nx][ym] = 2
                    q.append((nx, ym))


zero_case = list(combinations(zero, 3))
ans = 0
for case in zero_case:
    wall = copy.deepcopy(arr)

    for n, m in case:
        wall[n][m] = 1
    visited = copy.deepcopy(wall)
    for x, y in virus:
        bfs(x, y)
    total = 0
    for v in visited:
        total += v.count(0)

    ans = max(ans, total)

print(ans)
