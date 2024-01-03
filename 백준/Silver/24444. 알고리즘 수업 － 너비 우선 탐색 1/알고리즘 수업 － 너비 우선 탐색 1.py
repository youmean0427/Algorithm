import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs():
    q = [R]
    visited = [0] * (N+1)
    cnt = 1
    while q:
        x = q.pop(0)

        if visited[x] == 0:
            visited[x] = cnt

        arr[x].sort()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = cnt + 1
                cnt += 1

                q.append(i)

    return visited

x = bfs()
for i in range(1, len(x)):
    print(x[i])