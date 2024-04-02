import sys
from collections import defaultdict
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    now = input().rstrip()
    goal = input().rstrip()

    change = defaultdict(int)

    ans = 0
    for i in range(N):
        if now[i] != goal[i]:
            change[now[i]] += 1

    min_change = min(change["B"], change["W"])
    ans += min_change
    change["B"] -= min_change
    change["W"] -= min_change

    ans += change["B"] + change["W"]
    print(ans)