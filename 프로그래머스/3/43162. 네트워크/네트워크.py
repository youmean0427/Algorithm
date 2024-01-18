def solution(n, computers):
    p = [int(i) for i in range(n)]
    answer = 0
    
    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x])
        return p[x]
    
    def union(x, y):
        p[find_set(y)] = p[find_set(x)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                union(i, j)

    result = {}
    for i in p:
        result[find_set(i)] = 1

    answer = len(result)
    return answer
