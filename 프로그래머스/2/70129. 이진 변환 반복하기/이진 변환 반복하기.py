def solution(s):
    answer = []
    
    zero = 0
    cnt = 0
    
    while len(s) != 1:
        case = ""
        zero_cnt = 0
        for i in s:
            if i == "1":
                case += "1"
            else:
                zero_cnt += 1
        zero += zero_cnt
        s = bin(len(s)-zero_cnt)[2:]
        cnt += 1
        
    answer = [cnt, zero]
    return answer