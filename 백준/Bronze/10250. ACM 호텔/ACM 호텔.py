T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        result = H
        result2 = int(N / H)
    else:
        result = N % H
        result2 = (N // H) + 1
    # print(result, result2)


    if result2 < 10:
        result2 = '0' + str(result2)
    else:
        result2 = str(result2)

    print(str(result) + result2)
