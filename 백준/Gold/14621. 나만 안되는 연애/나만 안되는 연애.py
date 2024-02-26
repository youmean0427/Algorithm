import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().split())

node_s = {}
arr = [[] for _ in range(N+1)]

for i in range(0, N):
    node_s[i+1] = S[i]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))

def prim(start):

    heap = []
    heapq.heappush(heap, (0, start))

    visited = [0] * (N+1)
    key = [float('inf')] * (N+1)

    while heap:
        cost, node = heapq.heappop(heap)
        now_s = node_s[node]

        if visited[node] == 0:
            visited[node] = 1
            key[node] = cost
            for c, n in arr[node]:
                if visited[n] == 0 and node_s[n] != now_s:
                    heapq.heappush(heap, (c, n))

    if float('inf') in key[1:]:
        return -1
    return sum(key[1:])

x = prim(1)
print(x)
