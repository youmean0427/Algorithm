def solution(n, t, m, p):
    alpha = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    def change(x):
        arr = []
        while x >= n:
            if 9 < x % n < 16:
                arr.append(alpha[x%n])
            else:
                arr.append(x%n)
            x //= n
        if 9 < x % n < 16:
            arr.append(alpha[x])
        else:
            arr.append(x)
        arr.reverse()
        return arr
        
    answer = ''
    end = t * m
    box = []
    for i in range(end):
        box += change(i)
    
    for i in range(p-1, end, m):
        answer += str(box[i])
    
    return answer