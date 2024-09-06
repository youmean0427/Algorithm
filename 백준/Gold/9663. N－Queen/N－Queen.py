import sys
input = sys.stdin.readline

def can_go(x):

    for y in range(x):
        if (arr[y] == arr[x] or abs(arr[x] - arr[y]) == abs(x - y)):
            return False
    return True

def dfs(x):
    global ans

    if (x == n):
        ans += 1
        return

    for y in range(n):
        arr[x] = y
        if can_go(x):
            dfs(x + 1)


n = int(input())
arr = [float('inf') for _ in range(n)]
ans = 0
dfs(0)
print(ans)
