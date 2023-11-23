import sys
input = sys.stdin.readline
import heapq
"""
6 8
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 6 1
5 4 2
5 6 5
"""

def Dijkstra(s):
    heap = []
    D[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:

        x, y = heapq.heappop(heap)
        if D[y] < x:
            continue

        for i in arr[y]:
            cost = x + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

D = [float('inf')] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start, end = map(int, input().split())

Dijkstra(start)
print(D[end])
