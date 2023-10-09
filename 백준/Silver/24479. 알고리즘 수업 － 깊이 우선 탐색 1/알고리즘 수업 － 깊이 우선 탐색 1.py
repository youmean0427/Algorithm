import sys
input = sys.stdin.readline

def DFS(arr, start, N):
    cnt = 1
    stack = [start]
    visited = [0] * (N+1)
    result = [0] * (N+1)

    while stack:

        x = stack.pop()

        if visited[x] == 0:
            result[x] = cnt
            visited[x] = 1
            cnt += 1

        for i in range(len(arr[x])):
            if visited[arr[x][i]] == 0:
                stack.append(arr[x][i])

    return result


N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N+1):
    arr[i].sort(reverse=True)

result = DFS(arr, R, N)
for i in range(1, N+1):
    print(result[i])

