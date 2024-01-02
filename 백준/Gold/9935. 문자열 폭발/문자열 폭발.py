import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

S = input().rstrip()
B = input().rstrip()

S = S[::-1]
stack = []

i = 0
while i < len(S):
    stack.append(S[i])
    if "".join(stack[-1:-1-len(B):-1]) == B:
        for k in range(0, len(B)):
            stack.pop(-1)
    i += 1

if stack:
    print("".join(stack[::-1]))
else:
    print("FRULA")