import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().strip())))
answer = "NO"

def dfs(start, end):
    global answer
    stack = [(start, end)]

    while stack:
        x, y = stack.pop()
        if x == N-1:
            answer = "YES"
            return True
        if visited[x][y] == 0 and arr[x][y] == 0:
            visited[x][y] = 1

            for n, m in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx = n + x
                my = m + y
                if 0 <= nx < N and 0 <= my < M:
                    if arr[nx][my] == 0:
                        stack.append((nx, my))

visited = [[0 for _ in range(M)] for _ in range(N)]
for x in range(M):
    if dfs(0, x):
        break
print(answer)