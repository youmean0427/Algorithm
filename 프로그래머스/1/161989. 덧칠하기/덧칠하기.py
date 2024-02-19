def solution(n, m, section):
    answer = 0
    arr = [1] * (n+1) + [0] * m
    
    for i in section:
        arr[i] = 0
        
    idx = 1
    while idx <= n:
        if arr[idx] == 0:
            arr[idx:idx+m] = [1] * m
            idx +=  m
            answer += 1
        else:
            idx += 1
    
    return answer