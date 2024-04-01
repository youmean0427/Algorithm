import sys, math
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
ans = math.isqrt(N)
if ans**2 != N:
    ans += 1
print(ans)
