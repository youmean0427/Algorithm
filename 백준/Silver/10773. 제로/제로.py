import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    a = int(sys.stdin.readline())
    if a == 0 and stack:
        stack.pop(-1)
    else:
        stack.append(a)

print(sum(stack))