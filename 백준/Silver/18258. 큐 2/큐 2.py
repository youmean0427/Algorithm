import sys, math
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque([])
for _ in range(N):
    arr = [x for x in input().split()]

    if arr[0] == 'push':
        q.append(int(arr[1]))
    elif arr[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[0] == 'pop':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(q))
    elif arr[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif arr[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)