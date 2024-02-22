def solution(N, stages):
    answer = []
    fail = []
    S = len(stages)
    
    for i in range(1, N+1):
        if S:
            cnt = stages.count(i)
            fail.append((i, cnt / S))
            S -= cnt
        else:
            fail.append((i, 0))
        
    fail.sort(key=lambda x: -x[1])
    for i in fail:
        answer.append(i[0])
    return answer