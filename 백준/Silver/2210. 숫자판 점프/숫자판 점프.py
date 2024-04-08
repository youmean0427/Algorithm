import sys

# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

arr = [list(map(str, input().split())) for _ in range(5)]
ans = {}


def dfs(n, sm, x, y):
    if n >= 6 or len(sm) >= 6:
        res = "".join(sm)
        ans[res] = 1
        return

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for n, m in dir:
        nx = n + x
        my = m + y

        if 0 <= nx < 5 and 0 <= my < 5:
            dfs(n + 1, sm + [arr[x][y]], nx, my)


for n in range(5):
    for m in range(5):
        dfs(0, [], n, m)

print(len(ans))
