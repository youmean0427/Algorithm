import sys
input = sys.stdin.readline
from collections import deque

R, C, N = map(int, input().split())
arr = [[x for x in input().rstrip()] for _ in range(R)]

time = 1
q = deque()

def bfs(bomb):
    while bomb:

        x, y = bomb.pop()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        arr[x][y] = '.'

        for n, m in dir:
            xn = x + n
            ym = y + m
            if 0 <= xn < R and 0 <= ym < C:
                arr[xn][ym] = '.'
    return arr

while time <= N:

    if time % 2 == 0:
        arr = [['O'] * C for _ in range(R)]
        time += 1

    else:
        if q:
            bomb = q.popleft()
            bfs(bomb)

        q_sub = deque()
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    q_sub.append((i, j))
        q.append(q_sub)
        time += 1

for i in arr:
    print(''.join(i))