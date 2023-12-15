import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
def nm(n, sm):

    if n == M:
        result.append(sm)
        return

    for i in range(1, N+1):
        if str(i) not in sm:
            nm(n+1, sm + str(i))

nm(0, "")
for i in result:
    print(" ".join(i))