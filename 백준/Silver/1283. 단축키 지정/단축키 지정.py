import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):

    S = list(map(str, input().rstrip().split()))

    check = 0
    for i in range(len(S)):
        if S[i][0].upper() not in arr:
            arr.append(S[i][0].upper())
            S[i] = "[" + S[i][0] + "]" + S[i][1:]
            check = 1
            break

    check2 = 0
    if check == 0:
        for j in range(len(S)):
            for k in range(1, len(S[j])):
                if S[j][k].upper() not in arr:
                    arr.append(S[j][k].upper())
                    S[j] = S[j][:k] + "[" + S[j][k] + "]" + S[j][k+1:]
                    check2 = 1
                    break

            if check2 == 1:
                break

    print(*S)
