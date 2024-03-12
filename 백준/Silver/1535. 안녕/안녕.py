import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
s_hp = 100
s_joy = 0
ans = 0
hp = [int(i) for i in input().split()]
joy = [int(i) for i in input().split()]


def dfs(n, n_hp,n_joy):
    global ans
    if n >= N and n_hp > 0:
        ans = max(ans, n_joy)
        return

    if n_hp <= 0:
        return

    dfs(n+1, n_hp - hp[n], n_joy + joy[n])
    dfs(n+1, n_hp, n_joy)


dfs(0, s_hp, s_joy)
print(ans)