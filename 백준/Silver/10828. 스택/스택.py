import sys
input=sys.stdin.readline

N = int(input())
stack = list()

for _ in range(N):


    name = input()


    if name[0:4] == "push":
        stack.append(name[5:-1])

    elif name[0:3] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif name[0:4] == "size":
        print(len(stack))

    elif name[0:5] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif name[0:3] == "pop":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)

