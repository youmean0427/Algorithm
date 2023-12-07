import sys
input = sys.stdin.readline

cost = [25, 10, 5, 1]
result = [0] * 4
T = int(input())
for _ in range(T):
    C = int(input())
    for i in range(4):
        result[i] = C // cost[i]
        C = C % cost[i]
    print(*result)
