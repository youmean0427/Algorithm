from collections import deque

def solution(s):
    
    def check(s):
        right = 0
        stack = []
        for i in range(len(s)):
            x = s[i]
            if stack:
                if x == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif x == '}' and stack[-1] == '{':
                    stack.pop(-1)
                elif x == ')' and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(x)
            else:
                stack.append(x)        
        
        if stack == []:
            right = 1
        return right

    answer = 0
    x = deque(s)

    for i in range(len(s)):
        x.rotate(-1)
        answer += check(x)

    return answer

