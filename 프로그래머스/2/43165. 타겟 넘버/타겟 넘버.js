function solution(numbers, target) {
    let answer = 0
    
    function DFS(n, sm){
     
        if (n == N) {
            if (sm == target) {
                answer += 1
            }
            return
        }
        
        DFS(n+1, sm+numbers[n])
        DFS(n+1, sm-numbers[n])
        
    }
    
    const N = numbers.length
    DFS(0, 0)
    
    return answer;
}

