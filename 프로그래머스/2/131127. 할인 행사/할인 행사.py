def solution(want, number, discount):
    answer = 0
    buy = {}
    
    for i in range(len(want)):
        buy[want[i]] = number[i]

    for i in range(0, len(discount)-9):
        count = {}
        for j in range(i, i+10):
            if discount[j] in count:
                count[discount[j]] += 1
            else:
                count[discount[j]] = 1
        
        if (count == buy):
            answer += 1
    
    return answer