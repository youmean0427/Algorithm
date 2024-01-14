def solution(n):
    answer = 0
    dp = [0] * (n+1)
    
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    
    if n != 1:
        for i in range(3, n+1):
            dp[i] =  dp[i-1] + dp[i-2]
    
    answer = dp[n] % 1234567
    return answer