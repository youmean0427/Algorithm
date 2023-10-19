def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    pp = participant
    cp = completion
    
    p = 0
    c = 0
    
    while True:
        if c == len(cp):
            for i in pp:
                if i:
                    return i
        
        if pp[p] == cp[c]:
            pp[p] = ''
            cp[c] = ''
            
            p += 1
            c += 1
            
        else:
            p += 1
        