import sys
input = sys.stdin.readline

def divisor(x):
    div = []

    for i in range(1, x):
        if x % i == 0:
            div.append(i)

    if sum(div) == x:
        answer = str(x) + ' = '
        cnt = 0
        while cnt < len(div):
            answer += str(div[cnt])
            if cnt != len(div)-1:
                answer = answer + " + "
            cnt += 1
        return answer

    else:
        answer = str(x) + " is NOT perfect."
        return answer

while True:
    x = int(input())
    if x == -1:
        break

    result = divisor(x)
    print(result)