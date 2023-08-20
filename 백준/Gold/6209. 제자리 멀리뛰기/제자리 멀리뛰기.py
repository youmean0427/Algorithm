import sys
from itertools import combinations
input = sys.stdin.readline

d, n, m = map(int, input().split())
rocks = []

for _ in range(n):
    rocks.append(int(input()))
rocks.sort()
rocks.append(d)

start, end, ans = 0, d, 0

# mid가 거리의 최대값일 때, 바위 cnt개를 제거

while start <= end:
    cnt = 0
    now = 0
    mid = (start + end) // 2

    for j in rocks:
        if j - now < mid:
            cnt += 1
        else:
            now = j

    if cnt <= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)