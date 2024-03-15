import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

ans = 0
def dfs(n, sm):
    global ans
    if n >= N+1:
        if n == N+1:
            ans = max(ans, sm)
        return

    dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)

dfs(1, 0)
print(ans)