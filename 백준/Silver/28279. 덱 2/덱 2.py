import sys, math
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque([])
for _ in range(N):
    arr = [x for x in input().split()]
    N = int(arr[0])

    if N == 1:
        q.appendleft(int(arr[1]))
    elif N == 2:
        q.append(int(arr[1]))
    elif N == 3:
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif N == 4:
        if q:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif N == 5:
        print(len(q))
    elif N == 6:
        if q:
            print(0)
        else:
            print(1)
    elif N == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif N == 8:
        if q:
            print(q[-1])
        else:
            print(-1)