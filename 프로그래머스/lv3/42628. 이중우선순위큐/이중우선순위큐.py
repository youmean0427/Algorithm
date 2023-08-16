from collections import deque
def solution(operations):
    
    answer = []
    q = deque()

    for i in (operations):
        x, y = map(str, i.split()) 

        if x == 'I':
            if q and int(y) <= q[0]:
                q.appendleft(int(y))
            elif q and int(y) >= q[-1]:
                q.append(int(y))
            else:
                q.append(int(y))

        if x == 'D' and q:
            if y == '-1':
                q.popleft()
            if y == '1':
                q.pop()

    if len(q) >= 2:
        answer.append(max(q))
        answer.append(min(q))
    elif len(q) == 1:
        x = q.pop()
        answer.append(x)
        answer.append(x)
    else:
        answer.append(0)
        answer.append(0)

    return answer
