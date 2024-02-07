def solution(m, n, puddles):
    
    arr = [[0] * (m+1) for _ in range(n+1)]

    for x, y in puddles:
        arr[y][x] = 1 
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] == 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
    answer = dp[-1][-1] % 1000000007
    return answer