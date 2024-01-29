import math
def solution(str1, str2):
    def cut(x):
        arr = []
        for i in range(len(x)-1):
            if x[i].isalpha() and x[i+1].isalpha():
                arr.append(x[i] + x[i+1])
        return arr
    
    def inter(x, y):
        arr = []
        for i in x:
            if i in y:
                arr.append(i)
                y.remove(i)
        return arr
            
    def union(x, y):
        arr = []
        while x and y:
            
            p = x.pop(0)
            if p in y:
                y.remove(p)
                arr.append(p) 
            else:
                arr.append(p)
        
        arr += x
        arr += y
        return arr
  
    answer = 1
    str1 = str1.upper()
    str2 = str2.upper()
    x = inter(cut(str1), cut(str2))
    y = union(cut(str1), cut(str2))
    print(x, y)
    if len(x) != 0 and len(y) != 0:
        answer = (len(x) / len(y)) * 65536
    elif len(x) == 0 and len(y) != 0:
        answer = 0
    else:
        answer *= 65536
    
    answer = math.trunc(answer)
    return answer

