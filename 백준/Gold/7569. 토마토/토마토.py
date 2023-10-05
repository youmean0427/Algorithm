import sys
input = sys.stdin.readline
from collections import deque



M, N, H = map(int, input().split())
arr = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(H)]

# print(arr)
# print(visited)

q = deque()

def bfs():

    dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


    while q:

        z, y, x = q.popleft()


        for h, n, m in dir:
            zh = z + h
            yn = y + n
            xm = x + m

            if 0 <= zh < H and 0 <= yn < N and 0 <= xm < M:

                if arr[zh][yn][xm] == 0:
                    arr[zh][yn][xm] = arr[z][y][x] + 1
                    q.append((zh, yn, xm))



for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

bfs()
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            else:
                result = max(result, arr[i][j][k])

print(result-1)

