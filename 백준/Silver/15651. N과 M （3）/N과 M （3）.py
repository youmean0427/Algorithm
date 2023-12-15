import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
visited = [0] * (N+1)
def nm(n, sm):

    if n == M:
        result.append(sm)
        return

    for i in range(1, N+1):
        nm(n+1, sm + str(i))

nm(0, "")
for i in result:
    print(" ".join(i))