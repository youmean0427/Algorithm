from collections import deque
def solution(priorities, location):
    answer = 0
    arr = deque()
    for i in range(len(priorities)):
         arr.append((priorities[i], i))
    
    result = []
    while arr:
        x = arr.popleft()
        for i in arr:
            if i[0] > x[0]:
                arr.append((x[0], x[1]))
                break
        else:
            result.append(x[1])
            
    
    for i in range(len(result)):
        if result[i] == location:
            answer = i + 1

    return answer