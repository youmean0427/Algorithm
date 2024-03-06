import sys
from itertools import combinations
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

chicken = []
house = []

for n in range(N):
    for m in range(N):
        if arr[n][m] == 2:
            chicken.append((n, m))
        if arr[n][m] == 1:
            house.append((n, m))

cases = list(combinations(chicken, M))

ans = float('inf')
for case in cases:
    total = 0
    cnt = {}
    for c in case:
        for hn, hm in house:
            if (hn, hm) in cnt:
                cnt[(hn, hm)] = min(cnt[hn, hm],abs(c[0] - hn) + abs(c[1] - hm) )
            else:
                cnt[(hn, hm)] = abs(c[0] - hn) + abs(c[1] - hm)

    cnt_sum = sum(cnt.values())
    ans = min(ans, cnt_sum)

print(ans)