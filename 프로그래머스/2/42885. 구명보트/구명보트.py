def solution(people, limit):
    
    people.sort()
    start = 0
    cnt = 0
    end = len(people) - 1
    
    while start <= end:
        
        if people[start] + people[end] <= limit:
            cnt += 1
            start += 1
            end -= 1
        else:
            cnt += 1
            end -= 1
            
    return cnt