import sys
from collections import deque
from itertools import combinations
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
zero = []
virus = []

def arr_input():

    for i in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
        for j in range(len(line)):
            if line[j] == 0:
                zero.append((i, j))
            elif line[j] == 2:
                virus.append((i, j))

def bfs(sn, sm, wall):

    q = deque([(sn, sm)])
    wall[sn][sm] = 2

    while q:
        x, y = q.popleft()
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for n, m in dir:
            nx = n + x
            ym = y + m
            if 0 <= nx < N and 0 <= ym < M:
                if wall[nx][ym] == 0:
                    wall[nx][ym] = 2
                    q.append((nx, ym))

def wall_case():

    ans = 0
    zero_case = list(combinations(zero, 3))
    for case in zero_case:
        # wall = copy.deepcopy(arr)
        wall = [r[:] for r in arr]
        for n, m in case:
            wall[n][m] = 1

        for x, y in virus:
            bfs(x, y, wall)

        total = 0
        for v in wall:
            total += v.count(0)

        ans = max(ans, total)
    return ans

arr_input()
print(wall_case())