def solution(n):
    answer = 0
    
    def check(n):
        if n == 1:
            return False

        for i in range(2, int(n ** (1/2))+1):
            if n % i == 0:
                return False
        return True
    
    
    for i in range(1, n+1):
        if check(i):
            answer += 1

    return answer