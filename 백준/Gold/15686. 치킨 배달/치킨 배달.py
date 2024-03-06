import sys
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

visited = [0] * (N+1)
def dfs(cnt, sm, i):
    global ans
    if len(sm) == M:
        total = 0
        for hn, hm in house:
            min_dist = float('inf')
            for case in sm:
                dist = abs(case[0]-hn) + abs(case[1]-hm)
                min_dist = min(min_dist, dist)
            total += min_dist
        ans = min(total, ans)
        return

    if i == len(chicken):
        return

    dfs(cnt+1, sm+[chicken[i]], i+1)
    dfs(cnt+1, sm, i+1)


ans = float('inf')
dfs(0, [], 0)
print(ans)