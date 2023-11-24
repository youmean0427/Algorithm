import heapq

def solution(n, paths, gates, summits):
    def dijkstra():
        D = [float('inf')] * (n+1)
        heap = []

        for j in gates:
            heapq.heappush(heap, (0, j))
            D[j] = 0
                
        while heap:
            
            x, y = heapq.heappop(heap)
            
            
            if D[y] < x or y in summits:
                continue
            
            for i in arr[y]:
                cost = max(x, i[1])
                if cost < D[i[0]]:
                    D[i[0]] = cost
                    heapq.heappush(heap, (cost, i[0]))
                    
        for j in summits:
            min_inten.append([j, D[j]])
        

    answer = []
    arr = [[] for _ in range(n+1)]
    min_inten = []
    summits.sort()
    for i in paths:
        arr[i[0]].append((i[1], i[2]))  # (정점, 가중치)
        arr[i[1]].append((i[0], i[2]))
        
    dijkstra()


    min_inten.sort(key = lambda x: x[1])
    answer = min_inten[0]
    return answer