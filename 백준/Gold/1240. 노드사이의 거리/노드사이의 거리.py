import sys
input = sys.stdin.readline

def bfs(start, end):

    q = [(0, start)]
    visited = [float('inf')] * (N+1)
    visited[start] = 0

    while q:
        cost, node = q.pop(0)
        for next_cost, next_node in arr[node]:
            cost_sum = cost + next_cost
            if visited[next_node] > cost_sum:
                visited[next_node] = cost_sum
                q.append((cost_sum, next_node))

    return visited[end]

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((c, b)) # (cost, node)
    arr[b].append((c, a))

for _ in range(M):
    start, end = map(int, input().split())
    ans = bfs(start, end)
    print(ans)