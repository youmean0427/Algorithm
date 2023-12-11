import sys, math
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    arr = [int(x) for x in input().split()]
    num = arr[0]

    if num == 1:
        stack.append(arr[1])
    elif num == 2:
        if stack:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif num == 3:
        print(len(stack))
    elif num == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif num == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)