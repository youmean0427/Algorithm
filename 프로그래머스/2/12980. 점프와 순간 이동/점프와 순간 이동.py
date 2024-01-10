import math
def solution(n):
    
    ans = 0
    while n > 1:
        a = math.trunc(n / 2)
        b = n % 2
        n= a
        ans += b
    
    ans += 1
    return ans