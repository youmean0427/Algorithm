def solution(k, dungeons):
    global answer
    
    def dfs(n, sm):
        global answer

        answer = max(answer, sum(visited))
        
        if n >= len(dungeons):
            return
        
        for i, v in enumerate(dungeons):
            if sm >= v[0] and visited[i] == 0:
                visited[i] = 1
                sm -= v[1]
                dfs(n+1, sm)
                sm += v[1]
                visited[i] = 0
    
    visited = [0] * len(dungeons)
    answer = -1
    dfs(0, k)
    return answer