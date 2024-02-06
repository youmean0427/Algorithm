T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    arr = []
    for i in range(len(S)):
        arr.append(S[i:])
    arr.sort()
    print(f'#{t+1} {arr[N-1]}')