import sys
input=sys.stdin.readline

N = int(input())
q = list()

for _ in range(N):


    name = input()


    if name[0:4] == "push":
        q.append(name[5:-1])

    elif name[0:3] == "top":
        if q:
            print(q[-1])
        else:
            print(-1)

    elif name[0:4] == "size":
        print(len(q))

    elif name[0:5] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif name[0:3] == "pop":
        if q:
            print(q.pop(0))
        else:
            print(-1)

    elif name[0:5] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    elif name[0:4] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)