def solution(sequence, k):
    answer = []
    N = len(sequence)
     
    i = 0
    j = 0
    result = sequence[0]
    length = float('inf')
    
    while i < N:
        
        if result == k:
            if (i - j) < length:
                answer = [j, i]
                length = (i - j)
            result -= sequence[j]
            j += 1
        
        elif result < k:
            i += 1
            if i < N:
                result += sequence[i]
            
        elif result > k:
            result -= sequence[j]
            j += 1 
    
    return answer