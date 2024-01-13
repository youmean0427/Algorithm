def solution(arr):
    arr.sort()
    answer = 0
    i = 1
    y = arr[i]
    
    while i <= len(arr):
        x = LCM(y, arr[i-1])
        y = x
        i += 1
        
    return y

def GCD (a, b):
    while b:
        a, b = b, a % b
    return a

def LCM (a, b):
    return a * b / GCD(a, b)
    