def solution(people, limit):
    cnt = 0
    people.sort()
    
    i = 0
    j = len(people)-1
    
    while i <= j:
        if i == j:
            cnt += 1
            break
            
        if people[i] + people[j] > limit:
            cnt += 1
            j -= 1
          
        else:
            cnt += 1
            j -= 1
            i += 1
    
    return cnt