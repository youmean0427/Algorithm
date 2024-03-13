import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

arr = [int(i) for i in input().split()]
select = [1, 2, 3, 4, 5]
ans = 0


def dfs(n, sm, con):
    global ans
    if n >= len(arr):
        if sm >= 5:
            ans += 1
        return

    con_num = 0
    if len(con) >= 2:
        if con[-2] == con[-1]:
            con_num = con[-1]

    for i in select:
        if con_num == 0 or con_num != i:
            if arr[n] == i:
                dfs(n+1, sm+1, con+[i])
            else:
                dfs(n+1, sm, con+[i])


dfs(0, 0, [])
print(ans)