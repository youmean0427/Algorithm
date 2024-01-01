import math

def solution(progresses, speeds):
    time = []
    answer = {}
    for i in range(len(progresses)):
        time.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    answer[time[0]] = 1
    val = time[0]
    for i in range(1, len(time)):
        
        if val >= time[i]:
            pass      
        else:
            val = time[i]
            
        if val in answer:
            answer[val] += 1
        else:
            answer[val] = 1
            
    result = []
    for i in answer.values():
        result.append(i)
    return result