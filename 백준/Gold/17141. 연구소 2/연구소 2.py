import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
zero = []

for i in range(N):
    x = list(map(int, input().split()))
    for k in range(len(x)):
        if x[k] == 2:
            zero.append((i, k))
    arr.append(x)

virus = list(combinations(zero, M))

def bfs(x, y):

    q = [(x, y)]
    visited[x][y] = 1

    while q:

        n, m = q.pop(0)
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r, c in dir:
            nr = n + r
            mc = m + c
            if 0 <= nr < N and 0 <= mc < N:
                if arr[nr][mc] == 0 or arr[nr][mc] == 2:
                    if visited[nr][mc] == 0:
                        visited[nr][mc] = visited[n][m] + 1
                        q.append((nr, mc))
                    if visited[nr][mc]:
                        if visited[nr][mc] > visited[n][m] + 1:
                            visited[nr][mc] = visited[n][m] + 1
                            q.append((nr, mc))

def max_check(visited):
    max_val = 0
    for i in visited:
        if 0 in i:
            return -1
        else:
            max_val = max(max_val, max(i))
    return max_val


def visited_arr(N):
    visited = []
    for n in range(N):
        box = []
        for m in range(N):
            if arr[n][m] == 1:
                box.append(-1)
            else:
                box.append(0)
        visited.append(box)
    return visited

ans = 0
answer = float('inf')

for v in virus:
    visited = visited_arr(N)
    for x, y in v:
        bfs(x, y)
    cnt = max_check(visited)
    if cnt != -1:
        answer = min(answer, cnt)

if answer == float('inf'):
    ans = -1
else:
    ans = answer-1

print(ans)
