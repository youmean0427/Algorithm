
def dfs(n, sm):
    global ans

    if sm >= B:
        ans = min(sm, ans)
        return

    # 종료 조건
    if n == N:
        if sm >= B:
            ans = min(sm, ans)
        return

    dfs(n+1, sm + arr[n]) # 포함
    dfs(n+1, sm)          # 미포함


T = int(input())
for i in range(0, T):
    N, B = map(int, input().split())
    ans = float('inf')
    arr = [int(x) for x in input().split()]
    dfs(0, 0)
    print(f"#{i+1} {ans-B}")