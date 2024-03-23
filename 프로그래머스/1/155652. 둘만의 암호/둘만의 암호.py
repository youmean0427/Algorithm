def solution(s, skip, index):
    answer = ''
    for i in range(len(s)):
        arr = []
        cnt = 0
        while len(arr) <= index:
            x = ord(s[i]) + cnt

            while x >= 123:
                x = x % 97 + 71
                
            if chr(x) in skip:
                pass
            else:
                arr.append(chr(x))

            cnt += 1
        answer += arr[-1]
    return answer