import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
start = (0, 0)

def dfs(start):
    x, y = start[0], start[1]

    visited[x][y] = 1
    if arr[x][y] == -1:
        return


    dir = [(arr[x][y], 0), (0, arr[x][y])]

    for n, m in dir:
        nx = n+x
        my = m+y
        if 0 <= nx < N and 0 <= my < N and visited[nx][my] == 0:
            dfs((nx, my))


dfs(start)
if visited[N-1][N-1] == 1:
    print("HaruHaru")
else:
    print("Hing")