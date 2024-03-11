import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

H, N = map(int, input().split())
W = max(H, N) + 2
M = min(H, N)
arr = [[0 for _ in range(W)] for _ in range(W)]

arr[M+1][M] = 1
for i in range(M+1, W):
    for j in range(M+1, W):
        if i >= j:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[-1][-1])