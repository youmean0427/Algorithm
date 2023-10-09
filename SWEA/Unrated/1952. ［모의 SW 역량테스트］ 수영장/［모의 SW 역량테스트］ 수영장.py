def dfs(n, sm):
    global ans

    if n >= 12:
        ans = min(ans, sm)
        return

    dfs(n+1, sm + (cost[0] * arr[n]))
    dfs(n+1, sm + cost[1])
    dfs(n+3, sm + cost[2])
    dfs(n+12, sm + cost[3])


T = int(input())
for i in range(0, T):
    cost = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    ans = float('inf')

    dfs(0, 0)
    print(f"#{i+1} {ans}")