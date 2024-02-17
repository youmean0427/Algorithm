def solution(n):
            
    def prime_list(n):
        arr = [True] * (n+1)
        arr[0], arr[1] = False, False
        for i in range(2, n+1):
            if arr[i]:
                for j in range(i+i, n+1, i):
                    arr[j] = False
        
        cnt = 0
        for i in arr:
            if i:
                cnt += 1
        return cnt
    
    answer = prime_list(n)
    return answer