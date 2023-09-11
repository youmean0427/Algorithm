import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]
sum_arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_arr[i][j] = - sum_arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] + arr[i-1][j-1]

for _ in range(M):
    section = [int(a) for a in input().split()]
    start, end = section[:2], section[2:]

    a = sum_arr[start[0]-1][end[1]]
    b = sum_arr[end[0]][start[1]-1]
    c = sum_arr[start[0]-1][start[1]-1]

    sub = a + b - c
    print(sum_arr[end[0]][end[1]] - sub)