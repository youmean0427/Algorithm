import sys, math
input = sys.stdin.readline

N = int(input())
sm = 1
def fac(N, sm):
    if N == 0:
        return sm
    sm *= N
    return fac(N-1, sm)

print(fac(N, sm))