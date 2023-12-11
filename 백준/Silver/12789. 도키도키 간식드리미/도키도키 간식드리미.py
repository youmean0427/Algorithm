import sys, math
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = deque([int(i) for i in input().split()])

result = deque([])
place = deque([])

def dokidoki():
    cnt = 1
    while arr:

        if place:
            if place[-1] == cnt:
                result.append(place.pop())
                cnt += 1
                continue

        if arr:
            x = arr.popleft()
            if cnt == x:
                result.append(x)
                cnt += 1
            else:
                place.append(x)

    while place:

        if place[-1] == cnt:
            result.append(place.pop())
            cnt += 1
        else:
            return "Sad"

    return "Nice"

print(dokidoki())