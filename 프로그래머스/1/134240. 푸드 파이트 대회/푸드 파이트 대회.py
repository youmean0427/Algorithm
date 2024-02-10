def solution(food):
    answer = ''
    
    for i in range(len(food)):
        food[i] = int(food[i] / 2) 
        while food[i]:
            answer += str(i)
            food[i] -= 1
    
    answer = answer + '0' + answer[::-1]
    return answer