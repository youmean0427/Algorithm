import sys, heapq
input = sys.stdin.readline

def djik(start):

    D = [float('inf')] * (N+1)
    D[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:

        cost, node = heapq.heappop(heap)

        if D[node] < cost:
            continue

        for next_cost, next_node in arr[node]:
            cost_sum = next_cost + cost
            if D[next_node] > cost_sum:
                D[next_node] = cost_sum
                heapq.heappush(heap, (cost_sum, next_node))

    return D

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((c, b)) # (cost, node)
    arr[b].append((c, a))

for _ in range(M):
    start, end = map(int, input().split())
    print(djik(start)[end])