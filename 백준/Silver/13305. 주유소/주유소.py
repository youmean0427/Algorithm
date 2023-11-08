import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
road = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]

min_cost = cost[0]
total = 0

for i in range(len(cost)-1):
    if min_cost > cost[i]:
        min_cost = cost[i]

    total += min_cost * road[i]

print(total)