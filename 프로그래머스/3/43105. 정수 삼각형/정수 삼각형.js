function solution(triangle) {
    var answer = 0;
    const N = triangle.length
    let dp = Array.from({length : N}, () => Array(N).fill(0))
    dp[0][0] = triangle[0][0]

    for (let i = 1; i < N; i++ ) {
        for (let j = 0; j < triangle[i].length; j++) {
            if (j !== 0) {
            dp[i][j] = Math.max(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])
            } else {
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            }
        }
    }
    answer = Math.max(...dp[dp.length-1])
    return answer;
}