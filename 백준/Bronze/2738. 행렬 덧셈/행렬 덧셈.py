import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(2*N):
    box = [int(x) for x in input().split()]
    arr.append(box)

result = []
for x, y in (zip(arr[:N], arr[N:])):
    result.append([a+b for a, b in zip(x, y)])

for i in result:
    print(*i)