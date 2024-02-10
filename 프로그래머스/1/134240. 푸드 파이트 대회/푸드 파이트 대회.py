def solution(food):
    answer = ''
    
    for i in range(len(food)):
        if food[i] > 1:
            food[i] = food[i] // 2 
        elif food[i] <= 1:
            food[i] = 0
     
    arr = []
    for i in range(len(food)):
        while food[i]:
            arr.append(str(i))
            food[i] -= 1
    
    answer = "".join(arr)  + "0"
    arr.reverse()
    answer += "".join(arr)
    
    return answer