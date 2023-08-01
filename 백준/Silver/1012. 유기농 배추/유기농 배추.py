import sys
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = list([0] * M for _ in range(N))
    visited = list([0] * M for _ in range(N))

    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
    # print(farm)

    count = 0

    for i in range(N):
        for j in range(M):

            if farm[i][j] == 1 and visited[i][j] == 0:
                q = [(i, j)]
                visited[i][j] = 1

                while q:
                    # print(q)
                    xi, yj = q.pop()
                    visited[xi][yj] = 1

                    for ni, nj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if 0 <= xi+ni < N and 0<= yj+nj < M:
                            if farm[xi+ni][yj+nj] == 1 and visited[xi+ni][yj+nj] == 0:
                                q.append((xi+ni, yj+nj))

                count += 1

    print(count)