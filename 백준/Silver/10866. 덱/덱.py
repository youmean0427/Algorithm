
from collections import deque
import sys
input=sys.stdin.readline


N = int(input())
deq = deque()

for _ in range(N):

    name = input()

    if name[0:10] == "push_front":
        deq.appendleft(name[11:-1])


    elif name[0:9] == "push_back":
        deq.append(name[10:-1])

    elif name[0:3] == "top":
        if deq:
            print(deq[-1])
        else:
            print(-1)

    elif name[0:4] == "size":
        print(len(deq))

    elif name[0:5] == "empty":
        if deq:
            print(0)
        else:
            print(1)

    elif name[0:9] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)

    elif name[0:8] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)

    elif name[0:5] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif name[0:4] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
