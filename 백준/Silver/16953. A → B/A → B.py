import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def dfs(n, sm):
    global res
    if sm > B:
        return

    if sm == B:
        res = min(res, n)
        return

    dfs(n+1, sm * 2)
    dfs(n+1, int(str(sm) + '1'))

res = float('inf')
dfs(0, A)

if res == float('inf'):
    print(-1)
else:
    print(res+1)
