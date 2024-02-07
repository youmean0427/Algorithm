import math
def solution(n, s):
    
    def find(n, s):
        x = math.ceil(s / n)
        return x
    if n > s:
        return [-1]
    
    cnt = n
    answer = []
    
    while cnt > 0:
        x = find(cnt, s)
        answer.append(x)
        s -= x
        cnt -= 1
    
    answer.sort()
    return answer