T = int(input())
m = ['a', 'e', 'i', 'o', 'u']
for t in range(T):
    s = list(input())
    answer = ''
    for i in s:
        if i not in m:
            answer += i
    print(f'#{t+1} {answer}')