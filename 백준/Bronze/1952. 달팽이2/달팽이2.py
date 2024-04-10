import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(M)]
start = [0, 0]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
total = 0

def dfs(start):
    global total
    stack = [start]
    idx = 0
    d = dir[idx]
    while stack:
        n, m = stack.pop()
        if arr[n][m] == 0:
            arr[n][m] = 1
            if 0 <= n+d[0] < M and 0 <= m+d[1] < N:
                if arr[n+d[0]][m+d[1]]:
                    idx += 1
                    d = dir[idx % 4]
                    total += 1
                    if 0 <= n + d[0] < M and 0 <= m + d[1] < N:
                        stack.append((n + d[0], m + d[1]))
                else:
                    stack.append((n+d[0], m+d[1]))
            else:
                idx += 1
                d = dir[idx % 4]
                total += 1
                if 0 <= n + d[0] < M and 0 <= m + d[1] < N:
                    stack.append((n+d[0], m+d[1]))
dfs(start)
print(total-1)