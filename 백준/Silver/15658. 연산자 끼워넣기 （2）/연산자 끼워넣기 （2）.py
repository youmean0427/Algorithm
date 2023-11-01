import sys
input = sys.stdin.readline

def dfs(n, sm):
    global max_val, min_val

    if n == N-1:
        max_val = max(max_val, sm)
        min_val = min(min_val, sm)
        return

    if op[0]:
        op[0] -= 1
        dfs(n+1, sm + arr[n+1])
        op[0] += 1

    if op[1]:
        op[1] -= 1
        dfs(n+1, sm - arr[n+1])
        op[1] += 1

    if op[2]:
        op[2] -= 1
        dfs(n+1, sm * arr[n+1])
        op[2] += 1

    if op[3]:
        op[3] -= 1
        if sm < 0:
            dfs(n+1, -1 * ((-1 * sm) // arr[n+1]))
        else:
            dfs(n+1, sm // arr[n+1])
        op[3] += 1

N = int(input())
arr = [int(x) for x in input().split()]
op = [int(x) for x in input().split()]
# 0 : +, 1 : -, 2 : x, 3 : //

max_val = -1000000000
min_val = 1000000000
dfs(0, arr[0])
print(max_val)
print(min_val)