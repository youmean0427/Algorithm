function solution(n) {
    let answer = 0;
    let dp = new Array(n+1).fill(0)

    if(n >= 1){
        dp[1] = 1
    }
    
    if (n >= 2) {
        dp[2] = 2
    }
    
    if (n !== 1) {
        for(let i = 3; i < n+1; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        }
    }
    
    answer = dp[n] % 1234567
    return answer;
}