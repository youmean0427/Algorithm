def solution(k, score):
    answer = []
    arr = []
    
    for i in score:
        if len(arr) < k+1:
            arr.append(i)
        arr.sort(reverse=True)
        
        if len(arr) > k:
            arr.pop()

        answer.append(arr[-1])

    return answer