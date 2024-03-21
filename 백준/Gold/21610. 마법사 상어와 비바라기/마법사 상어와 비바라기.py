import sys, math
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def cloud_move(x, y, d, s):
    global now_cloud
    dir = [(), [0, -s], [-s, -s], [-s, 0], [-s, s], [0, s], [s, s], [s, 0], [s, -s]]

    x += dir[d][0]
    y += dir[d][1]

    if x < 0:
        x = math.ceil(-x / N) * N + x
    elif x >= N:
        x = x % N
    if y < 0:
        y = math.ceil(-y / N) * N + y
    elif y >= N:
        y = y % N

    now_cloud.append((x, y))

def raniy(cloud, visited):
    for x, y in cloud:
        arr[x][y] += 1

    dir = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    while cloud:
        cn, cm = cloud.pop()
        visited[cn][cm] = 1
        for n, m in dir:
            cnn, cmm = cn + n, cm + m
            if 0 <= cnn < N and 0 <= cmm < N:
                if arr[cnn][cmm]:
                    arr[cn][cm] += 1
    return visited

def make_cloud(visited):
    new_cloud = []
    for n in range(N):
        for m in range(N):
            if visited[n][m] == 0:
                if arr[n][m] >= 2:
                    arr[n][m] -= 2
                    new_cloud.append((n, m))
    return new_cloud

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    now_cloud = []
    while cloud:
        x, y = cloud.pop()
        cloud_move(x, y,  d, s)

    cloud = now_cloud
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited = raniy(cloud, visited)
    cloud = make_cloud(visited)

ans = 0
for i in arr:
    ans += sum(i)
print(ans)