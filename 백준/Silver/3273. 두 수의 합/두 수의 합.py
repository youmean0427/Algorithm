import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = [int(x) for x in input().split()]
x = int(input())

arr.sort()

start = 0
end = N-1
cnt = 0
while start != end:
    if arr[start] + arr[end] == x:
        end -= 1
        cnt += 1
    else:
        if arr[start] + arr[end] < x:
            start += 1
        else:
            end -= 1

print(cnt)