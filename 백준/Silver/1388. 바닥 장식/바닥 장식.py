import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    arr.append(list(input().rstrip()))

def dfs(sn, sm):

    if arr[sn][sm] == '-':
        type = 1
        dir = [0, 1]
    else:
        type = 2
        dir = [1, 0]

    stack = [(sn, sm)]
    while stack:
        x, y = stack.pop()

        if visited[x][y] == 0:
            visited[x][y] = 1

            dx, dy = x + dir[0], y + dir[1]
            if 0 <= dx < N and 0 <= dy < M:
                if visited[dx][dy] == 0:
                    if (type == 1 and arr[dx][dy] == '-') or (type == 2 and arr[dx][dy] == '|'):
                        stack.append((dx, dy))

answer = 0
for a in range(N):
    for b in range(M):
        if visited[a][b] == 0:
            dfs(a, b)
            answer += 1

print(answer)