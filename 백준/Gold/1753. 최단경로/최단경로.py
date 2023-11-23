import sys
input = sys.stdin.readline
import heapq

def dij(start):

    heap = []
    heapq.heappush(heap, (0, start))
    D[start] = 0

    while heap:
        w, u = heapq.heappop(heap)

        if D[u] < w:
            continue

        for i in arr[u]:
            cost = w + i[1]
            if D[i[0]] > cost:
                D[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V+1)]
D = [float('inf')] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))

dij(K)
for i in D[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)