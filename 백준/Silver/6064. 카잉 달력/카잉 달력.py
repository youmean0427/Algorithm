import sys
input = sys.stdin.readline
from math import lcm

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = -1
    for i in range(0, lcm(M, N), M):
        if ((i + x) - x) % M == 0 and ((i + x)-y) % N == 0:
            cnt = i+x
            break

    print(cnt)
