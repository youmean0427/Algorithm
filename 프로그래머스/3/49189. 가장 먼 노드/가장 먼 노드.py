import heapq
def solution(n, edge):
    arr = [[] for _ in range(n + 1)]
    key = [0] * (n + 1)
    answer = 0

    for x, y in edge:
        arr[x].append((1, y))
        arr[y].append((1, x))

    def prim():
        heap = []
        heapq.heappush(heap, (0, 1))

        visited = [0] * (n+1)
        visited[1] = 1
        while heap:

            cost, node = heapq.heappop(heap)
            for next_cost, next_node in arr[node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    key[next_node] = cost + next_cost
                    heapq.heappush(heap, (cost + next_cost, next_node))

    prim()
    max_value = max(key)
    for val in key:
        if val == max_value:
            answer += 1

    return answer