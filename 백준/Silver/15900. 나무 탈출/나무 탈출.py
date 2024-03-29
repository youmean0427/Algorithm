import sys
# sys.stdin = open("input.txt", 'r')
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

leaf = 0
def dfs(start):
    global leaf
    depth = 0
    visited = [0] * (N+1)
    stack = [(start, depth)]
    while stack:

        x, d = stack.pop()

        if len(arr[x]) == 1:
            leaf += d

        if visited[x] == 0:
            visited[x] = 1
            for i in arr[x]:
                if visited[i] == 0:
                    stack.append((i, d+1))

dfs(1)
if leaf % 2 == 1:
    print("Yes")
else:
    print("No")