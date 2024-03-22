def solution(maps):
    answer = -1

    N, M = len(maps), len(maps[0])
    for n in range(N):
        for m in range(M):
            if maps[n][m] == "S":
                start = (n, m)
            elif maps[n][m] == "L":
                lever = (n, m)
            elif maps[n][m] == "E":
                end = (n, m)
                
    def bfs(sn, sm, en, em):
        visited = [[float("inf") for _ in range(M)] for _ in range(N)]
        q = [(sn, sm)]
        visited[sn][sm] = 1
        
        while q:
            x, y = q.pop(0)
            if x == en and y == em:
                return visited[en][em]
            
            dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for n, m in dir:
                nx, my = n+x, m+y
                if 0 <= nx < N and 0 <= my < M:
                    if maps[nx][my] != "X":
                        if visited[nx][my] == float('inf'):
                            visited[nx][my] = min(visited[nx][my], visited[x][y]+1)
                            q.append((nx, my))

    start_to_lever = bfs(start[0], start[1], lever[0], lever[1])
    lever_to_end = bfs(lever[0], lever[1], end[0], end[1])
                
    if start_to_lever != None and lever_to_end != None:
        answer = start_to_lever - 1 + lever_to_end - 1
    
    return answer