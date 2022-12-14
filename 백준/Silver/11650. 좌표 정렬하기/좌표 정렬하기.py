import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort()
# print(arr)
for i in arr:
    print(i[0], i[1])

