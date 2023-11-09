import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

S = input().rstrip()
S = list(S)
lenS = len(S)
result = []
cnt = 0

while S:

    x = S.pop(0)
    if x == 'q':
        result.append([x])

    flag = 1
    i = 0
    
    while i < len(result) and flag:
        
        if result[i][-1] == "q" and x == 'u':
            result[i].append(x)
            flag = 0
            break
        elif result[i][-1] == "u" and x == 'a':
            result[i].append(x)
            flag = 0
            break
        elif result[i][-1] == "a" and x == 'c':
            result[i].append(x)
            flag = 0
            break
        elif result[i][-1] == "c" and x == 'k':
            result[i].append(x)
            flag = 0
            break
        elif result[i][-1] == "k" and x == 'q':
            result[i].append(x)
            flag = 0
            
        i += 1

check = 0
q_check = 0
len_check = 0

for i in result:
    if i[len(i)-5:len(i)] == ['q', 'u', 'a', 'c', 'k']:
       cnt += 1
       check = 1
       
       q_check += i.count('q')
       len_check += len(i)
       
    elif 'u' in i or 'a' in i or 'c' in i or 'k' in i:
        print(-1)
        exit(0)

if lenS > len_check:
    print(-1)
    exit(0)

if check == 1 and q_check == len(result):
    print(cnt)
else:
    print(-1)