def solution(k, tangerine):
    answer = 0
    cnt = {}
    for i in tangerine:
        cnt[i] = cnt[i] + 1 if i in cnt else 1

    cnt = sorted(cnt.items(), key = lambda x: -x[1])
    
    ans = []
    while k > 0:
        x, y = cnt.pop(0)
        k -= y
        ans.append(x)
        
    answer = len(ans)    
    return answer