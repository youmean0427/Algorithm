def solution(n):
    answer = 0
    
    def prime(n):
        for i in range(2, int(n ** (1/2))+1):
            if n % i == 0:
                return False
        return True
    
    for i in range(2, n+1):
        if prime(i):
            answer += 1

    return answer