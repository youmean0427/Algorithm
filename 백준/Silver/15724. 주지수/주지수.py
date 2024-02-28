import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())
prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    partial_sum = prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y] + prefix_sum[i-1][j-1]
    print(partial_sum)