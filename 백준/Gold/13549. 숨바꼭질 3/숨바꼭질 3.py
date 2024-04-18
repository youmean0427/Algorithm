import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [float('inf')] * 100001
ans = float('inf')
def bfs(n, sec):
    global ans
    q = deque([(n, sec)])
    dp[n] = 0
    while q:

        x, y = q.popleft()

        if x == K:
            ans = min(ans, y)


        if x+1 <= 100000:
            if dp[x+1] > y+1:
                dp[x+1] = y+1
                q.append((x + 1, y + 1))
        if x-1 >= 0:
            if dp[x-1] > y+1:
                dp[x-1] = y+1
                q.append((x - 1, y + 1))
        if 0 <= 2 * x <= 100000:
            if dp[2*x] > y:
                dp[2*x] = y
                q.append((2 * x, y))

bfs(N, 0)
print(ans)
