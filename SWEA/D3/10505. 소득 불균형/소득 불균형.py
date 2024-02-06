T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    avg = sum(arr) / len(arr)
  	
    answer = 0
    for i in arr:
        if i <= avg:
            answer += 1
    
    print(f'#{t+1} {answer}')
