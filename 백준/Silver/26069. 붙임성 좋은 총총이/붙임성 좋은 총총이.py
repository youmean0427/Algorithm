import sys, math
input = sys.stdin.readline

N = int(input())
result = {"ChongChong"}

for _ in range(N):
    A, B = [i for i in input().split()]
    if A in result or B in result:
        result.add(A)
        result.add(B)

print(len(result))