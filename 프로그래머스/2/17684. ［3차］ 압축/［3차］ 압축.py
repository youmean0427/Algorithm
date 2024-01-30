def solution(msg):
    answer = []
    alpha = {}
    
    for i in range(65, 65+26):
        alpha[chr(i)] = i - 64
    cnt = 27
    
    i = 0
    while i < len(msg):
        find = msg[i]
        j = i+1
        
        while j < len(msg):
            find += msg[j]
            
            if find in alpha:
                pass
            else:
                answer.append(alpha[find[0:len(find)-1]])
                alpha[find] = cnt
                cnt += 1
                break
                
            j += 1
            
        i = j

    answer.append(alpha[find])
    return answer