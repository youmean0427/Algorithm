def solution(n, k):
    answer = 0
    
    def change(x, k):
        arr = []
        while x >= k:
            arr.append(str(x % k))
            x //= k
        
        arr.append(str(x))
        arr.reverse()
        
        return "".join(arr)
        

    def prime(x):
        for i in range(2, int(x ** (1/2))+1):
            if x % i == 0:
                return False
        else:
            return True        
        
    x = change(n, k)
    y = x.split("0")

    for i in y:
        if i == "1" or i == '':
            pass
        else:
            if prime(int(i)): 
                answer += 1
        
    return answer