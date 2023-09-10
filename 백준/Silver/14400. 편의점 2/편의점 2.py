import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = []
for _ in range(N):
    x, y =  map(int, input().split())
    arr.append((x, y))

arr.sort()
a = ((arr[N//2][0]))
arr.sort(key = lambda x : x[1])
b = ((arr[N//2][1]))

total = 0
for n, m in arr:
    total += abs(a-n) + abs(b-m)

print(total)