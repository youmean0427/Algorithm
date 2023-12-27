def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, N):
        for j in range(len(triangle[i])):
            dp[i][j] = max(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])
    
    answer = max(dp[-1])
    return answer