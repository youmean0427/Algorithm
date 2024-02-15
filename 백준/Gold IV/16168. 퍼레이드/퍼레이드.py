import sys, copy
from collections import deque
input = sys.stdin.readline

v, e = map(int, input().split())
arr = [[] for _ in range(v+1)]
visited_dic = {}

for i in range(e):
    va, vb = map(int, input().split())
    arr[va].append(vb)
    arr[vb].append(va)
    visited_dic[(va, vb)] = 0
    visited_dic[(vb, va)] = 0

def dfs(start, visited):

    stack = deque([(0, start)])
    visited[(0, start)] = 0
    visited[(start, 0)] = 0

    while stack:
        pre, now = stack.pop()

        if visited[(pre, now)] == 0 and visited[(now, pre)] == 0:
            visited[(pre, now)] = 1
            visited[(now, pre)] = 1
            check = 0
            for i in arr[now]:
                if visited[(now, i)] == 0 and visited[(i, now)] == 0:
                    stack.append((now, i))
                    check = 1

            if check == 0:
                if 0 in visited.values():
                    return "NO"
                return "YES"

ans = "NO"
for i in range(1, v+1):
    visited = copy.copy(visited_dic)
    x = dfs(i, visited)
    if x == "YES":
        ans = x
        break

print(ans)