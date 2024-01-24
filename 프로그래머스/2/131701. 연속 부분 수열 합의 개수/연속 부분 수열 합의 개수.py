from collections import deque
def solution(elements):
    answer = 0
    ele = deque(elements)
    total = set() 
    for i in range(len(ele)):
        cnt = ele[0]
        total.add(cnt)
        for j in range(1, len(ele)):
            cnt += ele[j]
            total.add(cnt)
            
        ele.rotate(-1)

    answer = len(total)
    return answer