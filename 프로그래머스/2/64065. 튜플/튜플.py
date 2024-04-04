from collections import defaultdict
def solution(s):
    answer = []
    s = s.split("},{")
    N = len(s)
    
    s[0] = s[0].lstrip("{")
    s[N-1] = s[N-1].rstrip("}")
    
    for idx in range(len(s)):
        s[idx] = s[idx].split(",")
        
    s.sort(key= lambda x: len(x))
    cnt = defaultdict(int)
    
    for i in s[N-1]:
        cnt[i] += 1
        
    for n in range(N):
        for m in range(len(s[n])):
            if cnt[s[n][m]]:
                answer.append(int(s[n][m]))
                cnt[s[n][m]] -= 1
                
    return answer