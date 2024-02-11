def solution(cards1, cards2, goal):
    answer = "No"
    
    idx1, idx2, idxg = 0, 0, 0
    
    while idxg < len(goal):
        
        if idx1 < len(cards1) and cards1[idx1] == goal[idxg]:
            idx1 += 1
            idxg += 1
        
        elif idx2 < len(cards2) and cards2[idx2] == goal[idxg]:
            idx2 += 1
            idxg += 1
        
        else:
            break
        
    if idxg == len(goal):
        answer = "Yes"
        
    return answer