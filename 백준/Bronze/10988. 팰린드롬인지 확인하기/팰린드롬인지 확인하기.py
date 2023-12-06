import sys
input = sys.stdin.readline

S = input().rstrip()

if S == S[::-1]:
    print(1)
else:
    print(0)