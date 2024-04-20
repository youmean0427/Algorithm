import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n = int(input())
sn, en = map(int, input().split())
arr = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def bfs(sn):
    q = [(sn, 0)]
    visited = [0] * (n+1)
    while q:
        x, y = q.pop(0)

        if x == en:
            return y

        for di in arr[x]:
            if visited[di] == 0:
                visited[di] = 1
                q.append((di, y+1))

    return -1

ans = bfs(sn)
print(ans)