import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
x = pow(A, B, C)
print(x)