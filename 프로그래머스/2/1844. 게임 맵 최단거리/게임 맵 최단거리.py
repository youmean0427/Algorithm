def solution(maps):
    global ans
    
    ans = -1
    N = len(maps)
    M = len(maps[0])
    visited = [[0 for _ in range(M)] for _ in range(N)] 
    
    start = [0, 0]
    
    def bfs():
        global ans
        queue = [start]
        cnt = 1
        while queue:

            x, y = queue.pop(0)
            
            if x == N-1 and y == M-1:
                ans = visited[x][y] + 1
                
            
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for n, m in dir:
                nx, my = x + n, m + y
                if 0 <= nx < N and 0 <= my < M:

                    if visited[nx][my] == 0 and maps[nx][my] == 1:
                        visited[nx][my] = visited[x][y] + 1
                        queue.append((nx, my))
            
    x = bfs()
    return ans