from collections import defaultdict

def solution(N, stages):
    fail = {}
    answer = []
    cnt = defaultdict(int)
    S = len(stages)
    
    for i in stages:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    for i in range(1, N+1):
        if i - 1 not in cnt:
            pass
        else:
            S -= cnt[i-1]
        
        if S:
            fail[i] = cnt[i] / S
        else:
            fail[i] = 0

    sorted_items = sorted(fail.items(), key = lambda x: -x[1])
    for i in sorted_items:
        answer.append(i[0])
        
    return answer