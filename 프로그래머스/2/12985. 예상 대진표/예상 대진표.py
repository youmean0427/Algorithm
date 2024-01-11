def solution(n,a,b):
    answer = 1

    i, j = 0, 0
    if a < b:
        i = a
        j = b
    else:
        i = b
        j = a

    while  i+1 != j or (i % 2 == 0 and j % 2 != 0):
        if i % 2 != 0:
            i += 1
        if j % 2 != 0:
            j += 1
        
        i = i//2
        j = j//2
        
        answer += 1
    
    return answer