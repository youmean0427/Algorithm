function solution(numbers) {
    var answer = 0;
    const N = numbers.length
    let cases = new Set()
    let visited = new Array(N).fill(0) 
    
    function prime(x) {
        
        if (x === 1 || x === 0) {
            return false
        }
        
        for (let i = 2; i <= x ** (1/2); i++) {
            if (x % i === 0) {
                return false
            }
        }
        return true
    }
    
    
    function dfs(sm) {
        
        if (sm != '') {
            cases.add(parseInt(sm))
        }
        
        for (let i = 0; i < N; i++ ) {
            if (visited[i] == 0) {
                visited[i] = 1
                dfs(sm+numbers[i])
                visited[i] = 0
            }
        }    
    }
    
    dfs('')
    
    cases.forEach(x => {
        if (prime(x)) {
            answer++
        }
    })
    
    return answer;
}