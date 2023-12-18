import sys
input = sys.stdin.readline
from math import lcm

def find(M, N, x, y):
    for i in range(0, lcm(M, N), M):
        if ((i + x) - y) % N == 0:
            return i + x
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    ans = find(M, N, x, y)
    print(ans)
