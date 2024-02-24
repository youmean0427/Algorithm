def solution(numbers):
    global answer
    answer = 0
    visited = [0] * len(numbers)
    case = set()
    
    def prime(n):
        
        if n == 1 or n == 0:
            return False
        
        for i in range(2, int(n **(1/2))+1):
            if n % i == 0:
                return False
        return True
    
    def dfs(sm):

        if sm:
            case.add(int(sm))
        
        for i in range(len(numbers)):
            if visited[i] == 0:
                visited[i] = 1
                dfs(sm+numbers[i])
                visited[i] = 0
                
    dfs('')
    
    for i in case:
        if prime(i):
            answer += 1
    
    return answer