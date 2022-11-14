def DFS(n):

    stack = [n]
    visited = [0] * (N + 1)

    while stack:
        m = stack.pop()
        if visited[m] == 0:
            visited[m] = 1
            dfs.append(m)
            for i in range(N, 0, -1):
                if arr[m][i] == 1 and visited[i] == 0:
                    stack.append(i)

def BFS(n):

    queue = [n]
    visited = [0] * (N + 1)

    while queue:
        m = queue.pop(0)
        if visited[m] == 0:
            visited[m] = 1
            bfs.append(m)
            for i in range(0, N+1):
                if arr[m][i] == 1 and visited[i] == 0:
                    queue.append(i)


N, M, V = map(int, input().split())

arr = [[0] * (N+1) for _ in range(N+1)]
dfs = []
bfs = []

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

DFS(V)
print(*dfs)

BFS(V)
print(*bfs)
