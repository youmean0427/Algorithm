import sys
from itertools import combinations
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
build = [i for i in range(1, N+1)]
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

chicken = list(combinations(build, 2))

def dfs(sc1, sc2):
    visited = [float('inf')] * (N+1)
    stack = [(sc1, 0), (sc2, 0)]
    visited[sc1] = 1
    visited[sc2] = 1
    while stack:
        x, y = stack.pop()
        for i in arr[x]:
            if i != sc1 and i != sc2:
                if visited[i] > (y+1) * 2:
                    visited[i] = (y+1) * 2
                    stack.append((i, y+1))

    res = 0
    for i in visited:
        if i != 1 and i != float('inf'):
            res += i
    return res

chi = []
dis = float('inf')
for cc1, cc2 in chicken:
    res = dfs(cc1, cc2)
    if dis > res:
        dis = res
        chi = [cc1, cc2]

chi.sort()
print(*chi, dis)