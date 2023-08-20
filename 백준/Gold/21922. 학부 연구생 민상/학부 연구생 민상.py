import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]

ac = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            ac.append((i, j))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


total = 0
visited = [[0] * M for _ in range(N)]

def bfs(arr, q):
    global xx, yy, d_c
    while q:
        x, y = q.pop(0)

        xd, yd = xx + x, yy + y

        if 0 <= xd < N and 0 <= yd < M:
            if d_c == 0:
                if arr[xd][yd] == 0:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 1:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 2:
                    visited[xd][yd] = -1
                    break

                elif arr[xd][yd] == 3:
                    visited[xd][yd] = -1

                    d_c = 1
                    xx, yy = dir[1]
                    q.append((xd, yd))
                    continue
                elif arr[xd][yd] == 4:
                    visited[xd][yd] = -1

                    d_c = 3
                    xx, yy = dir[3]
                    q.append((xd, yd))
                    continue
            if d_c == 1:
                if arr[xd][yd] == 0:
                    visited[xd][yd] = -1
                    q.append((xd, yd))

                elif arr[xd][yd] == 1:
                    visited[xd][yd] = -1
                    break

                elif arr[xd][yd] == 2:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 3:
                    visited[xd][yd] = -1

                    d_c = 0
                    xx, yy = dir[0]
                    q.append((xd, yd))
                    continue

                elif arr[xd][yd] == 4:
                    visited[xd][yd] = -1

                    d_c = 2
                    xx, yy = dir[2]
                    q.append((xd, yd))
                    continue

            if d_c == 2:
                if arr[xd][yd] == 0:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 1:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 2:
                    visited[xd][yd] = -1
                    break

                elif arr[xd][yd] == 3:
                    visited[xd][yd] = -1

                    d_c = 3
                    xx, yy = dir[3]
                    q.append((xd, yd))
                    continue

                elif arr[xd][yd] == 4:
                    visited[xd][yd] = -1

                    d_c = 1
                    xx, yy = dir[1]
                    q.append((xd, yd))
                    continue

            if d_c == 3:
                if arr[xd][yd] == 0:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 1:
                    visited[xd][yd] = -1

                    break
                elif arr[xd][yd] == 2:
                    visited[xd][yd] = -1

                    q.append((xd, yd))

                elif arr[xd][yd] == 3:
                    visited[xd][yd] = -1

                    d_c = 2
                    xx, yy = dir[2]
                    q.append((xd, yd))
                    continue

                elif arr[xd][yd] == 4:
                    visited[xd][yd] = -1

                    d_c = 0
                    xx, yy = dir[0]
                    q.append((xd, yd))
                    continue


for n, m in ac:

    for d in range(4):

        q = [(n, m)]
        visited[n][m] = -1
        xx, yy = dir[d]
        d_c = d

        bfs(arr, q)


for i in visited:
    total += i.count(-1)
print(total)