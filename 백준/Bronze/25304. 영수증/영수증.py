import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

i = 0
total = 0
while i < N:
    a, b = map(int, input().split())
    total += a * b
    i += 1

if X == total:
    print("Yes")
else:
    print("No")