import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs():
    stack = [R]
    visited = [0] * (N+1)
    cnt = 1
    while stack:
        x = stack.pop()

        if visited[x] == 0:
            visited[x] = cnt
            cnt += 1
            arr[x].sort()
            for i in arr[x]:
                stack.append(i)

    return visited

x = dfs()
for i in range(1, len(x)):
    print(x[i])