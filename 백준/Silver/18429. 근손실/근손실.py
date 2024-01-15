import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(i) for i in input().split()]
ans = 0
visited = [0] * N

def dfs(n, sm):
    global ans
    if n >= N:
        if sm >= 500:
            ans += 1
        return

    if sm < 500:
        return

    for k in range(N):
        if visited[k] == 0:
            visited[k] = 1
            dfs(n+1, sm + arr[k] - K)
            visited[k] = 0

dfs(0, 500)
print(ans)