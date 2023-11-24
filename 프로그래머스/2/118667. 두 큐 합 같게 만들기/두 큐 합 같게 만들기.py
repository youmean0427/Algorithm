from collections import deque
def solution(queue1, queue2):
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    flag = len(queue1)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    N = (q1_sum + q2_sum) // 2
    
    if N < max(queue1) or N < max(queue2) or (q1_sum+q2_sum)% 2 != 0:
            return answer
    
    cnt = 0
    while q1_sum != q2_sum:
        if cnt >  flag * 4:
            return answer
        if q1_sum > q2_sum:
            x = queue1.popleft()
            queue2.append(x)
            q1_sum -= x
            q2_sum += x
            cnt += 1
        elif q1_sum < q2_sum:
            x = queue2.popleft()
            queue1.append(x)
            cnt += 1
            q1_sum += x
            q2_sum -= x
    
    answer = cnt
    return answer
