function solution(n) {
    let answer = 0;
    
    let i = 0
    let j = 0
    let cnt = 0
    
    while (i <= n) {

        i += 1
        cnt += i
        
        if (cnt == n) {
            answer += 1
            cnt = 0
            j += 1
            i = j
        } else if (cnt > n) {
            cnt = 0
            j += 1
            i = j
        }
        
        
    }
    return answer;
}