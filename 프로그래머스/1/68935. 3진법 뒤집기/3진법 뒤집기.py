def solution(n):
    def tentothree(n):
        x = ''
        while n >= 3:
            x += str(n % 3)
            n = n // 3
        x = (x + str(n))
        return x
        
    answer = int(tentothree(n), 3)
    return answer