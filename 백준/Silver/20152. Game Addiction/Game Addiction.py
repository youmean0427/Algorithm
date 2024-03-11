import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

H, N = map(int, input().split())
W = max(H, N) + 1
arr = [[0 for _ in range(W)] for _ in range(W)]

for n in range(W):
    for m in range(W):
        if m > n:
            arr[n][m] = -1

arr[min(H, N)][min(H, N)] = 1
for i in range(min(H, N), max(H, N)+1):
    for j in range(min(H, N), max(H, N)+1):
        if arr[i][j] == 0:
            if 0 <= i - 1 <= W and 0 <= j - 1 <= W:
                if arr[i-1][j] == -1 and arr[i][j-1] == -1:
                    continue
                elif arr[i - 1][j] == -1 and arr[i][j - 1] != -1:
                    arr[i][j] = arr[i][j-1]
                elif arr[i - 1][j] != -1 and arr[i][j - 1] == -1:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j]
            elif 0 <= i - 1 <= W:
                if arr[i-1][j] != -1:
                    arr[i][j] = arr[i-1][j]
            elif 0 <= j - 1 <= W:
                if arr[i][j-1] != -1:
                    arr[i][j] = arr[i][j-1]

print(max(arr[N][N], arr[H][H]))
