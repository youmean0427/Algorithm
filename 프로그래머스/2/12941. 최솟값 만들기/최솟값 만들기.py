def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
 
    for x,y in list(zip(A,B)):
        answer += x*y
        
    return answer