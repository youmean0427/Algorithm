def solution(land):
    answer = 0
    
    def dfs(x, y, g):
        
        stack = [(x, y)]
        check = set()
        check.add((x, y))
        cnt = 0
        
        while stack:
            a, b = stack.pop()

            if visited[a][b] == 0:
                cnt += 1
                visited[a][b] = 1
                
                for n, m in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    na = n + a
                    mb = m + b

                    if 0 <= na < N and 0 <= mb < M:
                        if land[na][mb] == 1:
                            stack.append((na, mb))
                            check.add((na, mb))
    
        for nn, mm in check:
            visited[nn][mm] = [len(check), g]
        
        return cnt
            
    
    
    N = len(land)
    M = len(land[0])
    
    dp = [0] * (M+1)
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    for m in range(M):
        for n in range(N):
            if land[n][m] == 1 and visited[n][m] == 0:
                x = (dfs(n, m, cnt))
                cnt += 1
    
    for m in range(M):
        box = []
        c = []
        for n in range(N):
            box.append(visited[n][m])
        
        for bb in box:
            if bb != 0:
                if bb[1] not in c:
                    c.append(bb[1])
                    dp[m] += bb[0]
    
    print(dp)
            
    answer = max(dp)
    return answer



