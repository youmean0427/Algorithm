def solution(sequence, k):
    answer = []
    N = len(sequence)
     
    i = 0
    j = 0
    result = sequence[0]
    
    while i < N:
        
        if result == k:
            answer.append((j, i, i - j))
            result -= sequence[j]
            j += 1
        
        elif result < k:
            i += 1
            if i < N:
                result += sequence[i]
            
        elif result > k:
            result -= sequence[j]
            j += 1 
    
    answer.sort(key=lambda x: x[2])
    answer = answer[0][:2]
    return answer