import sys
input = sys.stdin.readline

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

q = [(0, 0)]
visited = [[0] * N for _ in range(N)]
ans = 'Hing'

while q:

    a, b = q.pop()
    dir = [(0, arr[a][b]), (arr[a][b], 0)]

    for x, y in dir:

        ax = a + x
        by = b + y

        if ax == N-1 and by == N-1:
            ans = 'HaruHaru'
            break

        if 0 <= ax < N and 0 <= by < N:
            if visited[ax][by] == 0:
                visited[ax][by] = 1
                q.append((ax, by))

print(ans)
